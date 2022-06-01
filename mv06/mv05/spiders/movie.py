import scrapy

import operator
import time

import  sys
sys.path.append( r"E:\py\scrapy\mv05" )

from mv05.items import Mv05Item


#全局变量，已经获取downloadurl的id放入，如果已经存在，则不重复挖掘。
mvids = set()


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['xxx.com']
    start_urls = ['https://xxx.com']

    def parse(self, response):
        #result = response.xpath('/html/body/title/text()').extract_first()   /html/body/div/div/div/ul/li/div/div/
        result = response.xpath('//div[@class="item-menu"]/a/@href').extract()    #ul/li/div/div/div[@class="item-menu"]/a
        #print('-' * 60 )
        #print( result )
        #print('-' * 60)
        for url in result:
            url = self.fullUrl( url )
            yield scrapy.Request(url=url, callback=self.parseListPage )

        result = response.xpath('//li[@class="item-menu dropdown"]/div/div/div[@class="items-holder"]/div[@class="item"]/a/@href').extract()
        #print('-' * 60)
        #print(result)
        #print('-' * 60)
        for url in result:
            url = self.fullUrl(url)
            yield scrapy.Request(url=url, callback=self.parseListPage )

        result = response.xpath('//li[@class="item-menu dropdown"]/div/div/div[@class="items-holder tags"]/div[@class="item"]/a/@href').extract()
        #print('-' * 60)
        #print(result)
        #print('-' * 60)
        for url in result:
            url = self.fullUrl(url)
            yield scrapy.Request(url=url, callback=self.parseListPage )

        result = response.xpath(
            '//li[@class="item-menu dropdown"]/div/div/div[@class="items-holder models"]/div[@class="item"]/a/@href').extract()
        #print('-' * 60)
        #print(result)
        #print('-' * 60)
        for url in result:
            url = self.fullUrl(url)
            yield scrapy.Request(url=url, callback=self.parseListPage )

        result = response.xpath(
            '//li[@class="item-menu dropdown"]/div/div/div[@class="items-holder channels"]/div[@class="item"]/a/@href').extract()
        #print('-' * 60)
        #print(result)
        #print('-' * 60)
        for url in result:
            url = self.fullUrl(url)
            yield scrapy.Request(url=url, callback=self.parseListPage )

    def fullUrl(self, url ):
        #补充完整url， domain + path
        if not url.startswith("https://"):
            url = self.start_urls[0] + url
        return url

    def parseListPage(self, response ):
        #解析列表，获得mv信息和url
        global mvids

        result = response.xpath(
            '//div[@id="list_videos_common_videos_list_items"]/div[@class="item"]')
        #print('-' * 60)
        self.logger.info( "parseListPage item size : %d" % len( result ))
        #print('-' * 60)
        #pageUrl = response.url
        #mvs = []
        for e in result:
            data = Mv05Item()
            #print( e.xpath('./a[0]/@href').extract_first() )
            # data-rt="1:2c8d63ec93028cf593fa06c9ab7db742:0:164936:1:"
            data["id"] = e.xpath('./a/@data-rt').extract_first().split(":")[3]
            #if already exist，then jump
            if operator.contains( mvids, data["id"] ):
                continue

            data["url"] = e.xpath('./a/@href').extract_first()
            data["channel"] = getChannelFromURL(response.url)
            #data["channel"] = pageUrl    #"/"+ "/".join( pageUrl.split( "/" )[3:] )
            data["name"] = data["url"].split( "/")[-2]
            data["durat"] = e.xpath('./span/span[@class="durat info"]/text()').extract_first()
            data["rating"] = "".join( e.xpath('./a/div/span[@class="rating info"]/text()').extract()).strip( "\n\t")
            mvids.add( data["id"] )
            yield  data
            yield scrapy.Request(url=self.fullUrl( data["url"] ), callback=self.parsePlayPage )

        #解析分页，获取分页数据
        self.parsePagination( response )

    def parsePagination(self, response ):
        # 解析分页，获取分页数据

        #'//div[@class="pagination"]/ul/li[@class="item"]'
        result = response.xpath( '//ul[@class="pagination-holder"]/li[@class]' )
        print( result )
        if result and len( result ) > 0:
            # 获取最后一个分页数值。  如果有next button，则是倒数第2个；否则最后一个
            lastPageIdx = -1
            # css( '.next' )
            if result[ -1 ].xpath( '//li[contains(@class, "next")]' ):
                lastPageIdx = -2
            self.logger.info( lastPageIdx )
            lastPage = result[ lastPageIdx ]
            self.logger.info( lastPage.get()[ 0 : 300 ] )
            lastPageNum = lastPage.xpath( './a[@data-parameters]/text()' ).extract_first()
            self.logger.info( "获得分页数" + lastPageNum )

            pageparameters = lastPage.xpath( './a/@data-parameters' ).extract_first()
            self.logger.info( pageparameters[0:200] )
            params = makeDict( pageparameters )
            channel = getChannelFromURL( response.url )

            #默认获得第一页，跳过第一页
            for pidx in range( 2, int( lastPageNum ) +1 ):
                random =  '%d'%( time.time() )
                pagenum = self._makePageNum( pidx )
                #https://x.com/category/hd/?mode=async&function=get_block&block_id=list_videos_common_videos_list&sort_by=post_date&mode=async&rn=1864&from=02&_=1653161725163
                nextpageurl = 'https://{0}{1}?mode=async&function=get_block&block_id=list_videos_common_videos_list&sort_by=post_date&mode=async&rn={2}&from={3}&_={4}'.format(
                    self.allowed_domains[0], channel, params['rn'], pagenum, random )
                self.logger.info( nextpageurl )
                #yield  scrapy.Request(url=nextpageurl, callback=self.parseListPage )

    def _makePageNum(self , num ):
        return '%02d' % ( num )


    def parsePlayPage(self, response ):
        #具体mv播发页面，获取下载链接
        result = response.xpath(
            '//a[@class="link down"]')
        #print(result)
        data = Mv05Item()
        data["downloadurl"] = result.xpath( "./@href" ).extract_first()
        hd = result.xpath( "./text()" ).extract_first()
        #print( hd )
        data["length"] = hd.split(",")[-1].strip( " ")
        data["ipx"] = hd.split(",")[0].split( " ")[-1].replace( "p", "" )
        print( data )
        yield data

def getChannelFromURL( url ):
    #获取路径path，即 分类路径   返回 例如 /channel/digital/
    from urllib.parse import urlparse
    r = urlparse( url )
    return r.path

def makeDict( formatstring ):
    #"ss:xx;tt:yy;"  to  dict
    d = {}
    list = formatstring.replace(":", ";").strip(";").split( ";" )
    for i in range( 0, len(list), 2 ):
        d[ list[i] ] = list[i+1]
    return d



if __name__ == "__main__":
    from scrapy.http import HtmlResponse


    def home():
        with open( r"E:\迅雷下载\craw\home.html", 'r', encoding="UTF-8" ) as f:
            body = f.read()

        resp = HtmlResponse( "", body = body, encoding="UTF-8" )
        s = MovieSpider()
        s.parse( resp )

    def list():
        with open(r"E:\迅雷下载\craw\Digital.html", 'r', encoding="UTF-8") as f:
            body = f.read()

        resp = HtmlResponse("", body=body, encoding="UTF-8")
        s = MovieSpider()
        s.parseListPage(resp)

    #list()

    def p():
        with open(r"E:\迅雷下载\craw\play.html", 'r', encoding="UTF-8") as f:
            body = f.read()

        resp = HtmlResponse("", body=body, encoding="UTF-8")
        s = MovieSpider()
        s.parsePlayPage(resp)
    #p()

    def testpage():
        with open(r"E:\迅雷下载\craw\Digital.html", 'r', encoding="UTF-8") as f:
            body = f.read()

        resp = HtmlResponse("https://xxx.com/channel/digital/", body=body, encoding="UTF-8")
        s = MovieSpider()
        s.parsePagination(resp)


    #testpage()

    print( getChannelFromURL( "https://xxx.com/channel/digital/" ) )