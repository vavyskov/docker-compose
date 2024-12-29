from locust import task, run_single_user
from locust import FastHttpUser


class www_google_com(FastHttpUser):
    host = "https://www.google.com"
    default_headers = {
        "Accept-Language": "cs,sk;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=i&ei=VK1xZ4aFBLKKxc8Poea1iQU&ct=slh&v=t1&im=M&pv=0.20394962119200954&me=14:1735503512552,V,0,0,0,0:10462,e,H&zx=1735503523023&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/ss/k=xjs.hd.1HG8niZTeao.L.F4.O/am=CEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAAAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIAAgAwAgAMAAgAKAAAggRVAAgj4AAAlAAk98wGAAgEACAAIAAaUQUMgKgChABAAAAAAAABAAAAAQBAACAAAOgACwAAQCQCA6IEAAAAAAIIAAJATAJaBBwgAAAAAAACQAQAAAAwpIAAAAAAAAAAAAAAAAABEEAwFAAQEAAAAAAAAAAAAAAAAAACAQBME/d=1/ed=1/br=1/rs=ACT90oEuJKBfY6VuLOhgmh7m1ANPrbMj6g/m=cdos,hsm,jsa,mb4ZUb,cEt90b,SNUn3,qddgKe,sTsDMc,dtl0hd,eHDfl,YV5bee,d,csi",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/k=xjs.hd.cs.-ck81h5K_qM.es5.O/am=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAACgAAAAAAQAAAAABAAAAAAAAAAEAQiAAAAgAAAEwAIAAAQDgAAAAAIAABABwKNsARAgAgAwAAAgAIAAwgIAABAAAAAIAAAEAAAAKAAAAAAACAAAAAAABAAAQIAAAAAAAAAAAAAAAQAA6AEAAAAAAAAABAQAAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/d=1/ed=1/dg=3/br=1/rs=ACT90oF2ZClyn8ynmeovVy8S38ywKiHRhw/ee=ALeJib:B8gLwd;AfeaP:TkrAjf;BMxAGc:E5bFse;BgS6mb:fidj5d;BjwMce:cXX2Wb;CxXAWb:YyRLvc;DULqB:RKfG5c;Dkk6ge:JZmW9e;DpcR3d:zL72xf;EABSZ:MXZt9d;ESrPQc:mNTJvc;EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;EnlcNd:WeHg4;F9mqte:UoRcbe;Fmv9Nc:O1Tzwc;G0KhTb:LIaoZ;G6wU6e:hezEbd;GleZL:J1A7Od;HMDDWe:G8QUdb;HoYVKb:PkDN7e;HqeXPd:cmbnH;IBADCc:RYquRb;IoGlCf:b5lhvb;IsdWVc:qzxzOb;JXJSm:ii1RGf;JXS8fb:Qj0suc;JbMT3:M25sS;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;KOxcK:OZqGte;KQzWid:ZMKkN;KcokUb:KiuZBf;KpRAue:Tia57b;LBgRLc:SdcwHb,XVMNvd;LEikZe:byfTOb,lsjVmc;LXA8b:q7OdKd;LsNahb:ucGLNb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Np8Qkd:Dpx6qc;Nyt6ic:jn2sGd;OgagBe:cNTe0;OohIYe:mpEAQb;Pjplud:EEDORb,PoEs9b;Q1Ow7b:x5CSu;Q6C5kf:pfdZCe;QGR0gd:Mlhmy;R2kc8b:ALJqWb;R4IIIb:QWfeKf;R9Ulx:CR7Ufe;RCF5Sd:X1kBmd;RDNBlf:zPRCJb;SLtqO:Kh1xYe;SMDL4c:fTfGO,fTfGO;SNUn3:ZwDk9d,x8cHvb;ScI3Yc:e7Hzgb,e7Hzgb;ShpF6e:N0pvGc;SzQQ3e:dNhofb;TxfV6d:YORN0b;U96pRd:FsR04;UBKJZ:LGDJGb;UDrY1c:eps46d;UVmjEd:EesRsb;UVzb9c:IvPZ6d;Uvc8o:VDovNc;UyG7Kb:wQd0G;V2HTTe:RolTY;VGRfx:VFqbr;VN6jIc:ddQyuf;VOcgDe:YquhTb;VsAqSb:PGf2Re;VxQ32b:k0XsBb;WCEKNd:I46Hvd;WDGyFe:jcVOxd;Wfmdue:g3MJlb;XUezZ:sa7lqb;YIZmRd:A1yn5d;YV5bee:IvPZ6d;YkQtAf:rx8ur;ZSH6tc:QAvyLe;ZWEUA:afR4Cf;ZlOOMb:P0I0Ec;a56pNe:JEfCwb;aAJE9c:WHW6Ef;aCJ9tf:qKftvc;aZ61od:arTwJ;af0EJf:ghinId;bDXwRe:UsyOtc;bcPXSc:gSZLJb;cEt90b:ws9Tlc;cFTWae:gT8qnd;coJ8e:KvoW8;dIoSBb:ZgGg9b;dLlj2:Qqt3Gf;dowIGb:ebZ3mb,ebZ3mb;dtl0hd:lLQWFe;eBAeSb:Ck63tb;eBZ5Nd:audvde;eHDfl:ofjVkb;eO3lse:nFClrf;euOXY:OZjbQ;g8nkx:U4MzKc;gaub4:TN6bMe;gtVSi:ekUOYd;h3MYod:cEt90b;hK67qb:QWEO5b;heHB1:sFczq;hjRo6e:F62sG;hsLsYc:Vl118;iFQyKf:QIhFr,vfuNJf;imqimf:jKGL2e;jY0zg:Q6tNgc;k2Qxcb:XY51pe;kCQyJ:ueyPK;kbAm9d:MkHyGd;lOO0Vd:OTA3Ae;lbfkyf:MqGdUd;nAFL3:NTMZac,s39S4;nJw4Gd:dPFZH;oGtAuc:sOXFj;oSUNyd:fTfGO,fTfGO;oUlnpc:RagDlc;oVHXxc:HODIOb;okUaUd:wItadb;pKJiXd:VCenhc;pNsl2d:j9Yuyc;pXdRYb:JKoKVe;pj82le:ww04Df;qZx2Fc:j0xrE;qaS3gd:yiLg6e;qafBPd:sgY6Zb,yDVVkb;qavrXe:zQzcXe;qddgKe:d7YSfd,x4FYXe;rQSrae:C6D5Fc;ropkZ:UT1DG;sTsDMc:kHVSUb;sZmdvc:rdGEfc;tH4IIe:Ymry6;tosKvd:ZCqP3;trZL0b:qY8PFe;uuQkY:u2V3ud;vEYCNb:FaqsVd;vGrMZ:lPJJ0c;vfVwPd:lcrkwe;w3bZCb:ZPGaIb;w4rSdf:XKiZ9;w9w86d:dt4g2b;wQlYve:aLUfP;wR5FRb:O1Gjze,TtcOte;wV5Pjc:L8KGxe;xBbsrc:NEW1Qc;ysNiMc:CpIBjd;yxTchf:KUM7Z;z97YGf:oug9te;zOsCQe:Ko78Df;zaIgPb:Qtpxbd/m=cdos,hsm,jsa,mb4ZUb,cEt90b,SNUn3,qddgKe,sTsDMc,dtl0hd,eHDfl,YV5bee,d,csi",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://csp.withgoogle.com/csp/gws/other-hp",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Content-Length": "531",
                "Content-Type": "application/csp-report",
                "Host": "csp.withgoogle.com",
                "Origin": "https://www.google.com",
                "Priority": "u=4",
                "Sec-Fetch-Dest": "report",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            data='{"csp-report":{"blocked-uri":"inline","column-number":1,"disposition":"report","document-uri":"https://www.google.com/","effective-directive":"script-src-attr","original-policy":"object-src \'none\'; base-uri \'self\'; script-src \'nonce-ZFxxPkQMWCcEthnScWvfcQ\' \'strict-dynamic\' \'report-sample\' \'unsafe-eval\' \'unsafe-inline\' https: http:; report-uri https://csp.withgoogle.com/csp/gws/other-hp","referrer":"","script-sample":"_rtf(this)","source-file":"https://www.google.com/","status-code":200,"violated-directive":"script-src-attr"}}',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?ei=pK5xZ-eoBoWJ7NYPhfKrsAI&vet=10ahUKEwjnir645s2KAxWFBNsEHQX5CiYQhJAHCCU..s&bl=xroT&s=webhp&gl=cz&pc=SEARCH_HOMEPAGE&isMobile=false",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/gen_204?atyp=i&ct=bxjs&cad=&b=0&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&zx=1735503523274&opi=89978449",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=5, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/og/_/js/k=og.qtm.en_US.otmEBJ358uU.2019.O/rt=j/m=qabr,q_dnp,qcwid,qapid,qald,qads,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTu0yU9RTMfNNC-LVUmaaNKwIO136g",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?s=webhp&t=aft&atyp=csi&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&rt=wsrt.195,aft.310,hst.86,prt.310&imn=13&ima=0&imad=0&imac=3&wh=775&aft=1&aftp=-1&opi=89978449&r=1&ts=0",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://ogads-pa.googleapis.com/$rpc/google.internal.onegoogle.asyncdata.v1.AsyncDataService/GetAsyncData",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Content-Length": "66",
                "Content-Type": "application/json+protobuf",
                "Host": "ogads-pa.googleapis.com",
                "Origin": "https://www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "X-Goog-Api-Key": "AIzaSyCbsbvGCe7C9mCtdaTycZB2eUFuzsYKG_E",
                "X-User-Agent": "grpc-web-javascript/0.1",
            },
            data='[538,"",538,"cs","cz",0,null,0,0,"","",1,0,null,89978449,null,[1]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://apis.google.com/_/scs/abc-static/_/js/k=gapi.gapi.en.ZpMpph_5a4M.O/m=gapi_iframes,googleapis_client/rt=j/sv=1/d=1/ed=1/rs=AHpOoo_c5__TAiALeuHoQOKG0BnSpdbJrQ/cb=gapi.loaded_0",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "apis.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "apis.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=csi&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&s=webhp&t=all&imn=13&ima=0&imad=0&imac=3&wh=775&aft=1&aftp=-1&adh=&ime=2&imex=2&imeh=1&imeha=0&imehb=0&imea=0&imeb=0&imel=0&imed=0&imeeb=0&scp=0&cb=78037&ucb=258639&ts=78337&hp=&sys=hc.4&p=bs.true&rt=hst.86,prt.310,aft.310,aftqf.336,xjses.679,xjsee.778,xjs.778,lcp.234,fcp.213,wsrt.195,cst.0,dnst.0,rqst.107,rspt.0,sslt.0,rqstt.88,unt.2,ppunt.15,cstt.2,dit.546&zx=1735503523779&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/complete/search?q&cp=0&client=gws-wiz&xssi=t&gs_pcrt=2&hl=cs&authuser=0&psi=pK5xZ-eoBoWJ7NYPhfKrsAI.1735503523816&dpr=1&nolsbt=1",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/k=xjs.hd.cs.-ck81h5K_qM.es5.O/ck=xjs.hd.1HG8niZTeao.L.F4.O/am=CEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAQAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIQDgAwAgAMAAhALwKNsgRVgAgj4AAAlAIk98wOAAhEACAAIAAaUQUMgKgChABAACAAAAABABAAAQJAACAAAOgACwAAQCQCA6IEAAAAAAIIABJQTAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/d=0/dg=0/br=1/ujg=1/rs=ACT90oGgi79BR3Svmhox9DI0xWXV5v-Thw/m=sb_wiz,aa,abd,sy17o,syfz,syfr,syfp,syfq,syfs,syg0,syg1,syfw,syfv,syfu,syep,syft,syfj,syfi,syfk,syfh,syfm,sy16j,sygb,sy17m,syyl,syga,syg9,syg8,async,pHXghd,sf,sy3kv,syhl,syh1,sy3k7,sy3ka,sy277,sye3,sy9u,sy9f,sy9e,sy9c,spch,syti,syth,rtH1bd,sy19k,sy15l,sy151,sy12b,sydb,sy19i,SMquOb,sy7k,sy7j,syf3,syfe,syfc,syfb,syf2,syf0,syey,sy86,sy83,sy85,syex,syf1,syew,sybg,syb9,sybc,syaj,syap,syai,syah,syag,sya4,syba,syax,syay,syb4,syan,syb3,syaw,syat,syae,syal,syaz,sya6,sya8,sya9,sya5,syao,syad,syaa,sybj,sya0,sy9x,sybi,sy9p,sy9h,sy9k,sy9w,sya3,syb0,syev,syeu,syer,syeq,sy89,uxMpU,syem,sybq,sybo,sybk,syar,sybm,sybh,sy8n,sy8m,sy8l,sy8k,Mlhmy,QGR0gd,aurFic,sy8w,fKUV3e,OTA3Ae,sy7l,OmgaI,EEDORb,PoEs9b,Pjplud,sy8h,A1yn5d,YIZmRd,uY49fb,sy7b,sy79,sy75,sy78,sy77,sy76,byfTOb,lsjVmc,LEikZe,kWgXee,ovKuLd,sgY6Zb,sy8v,sy8y,sy88,xUdipf,NwH0H,gychg,ZfAoz,yDVVkb,qafBPd,ebZ3mb,dowIGb,sy19n,sy19l,syxi,sytn,d5EhJe,sy1a5,fCxEDd,syut,sy1a4,sy1a3,sy1a2,sy19u,sy19r,sy19s,sy17b,sy175,syx6,syx5,T1HOxc,sy19t,sy19q,zx30Y,sy1a7,sy1a6,sy19y,sy15y,Wo3n8,sysz,loL8vb,syt3,syt2,syt1,ms4mZb,sys1,B2qlPe,syue,NzU6V,syyx,sygo,zGLm3b?xjs=s3",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/k=xjs.hd.cs.-ck81h5K_qM.es5.O/ck=xjs.hd.1HG8niZTeao.L.F4.O/am=CEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAQAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIQDgAwAgAMAAhALwKNsgRVgAgj4AAAlAIk98wOAAhEACAAIAAaUQUMgKgChABAACAAAAABABAAAQJAACAAAOgACwAAQCQCA6IEAAAAAAIIABJQTAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/d=0/dg=0/br=1/ujg=1/rs=ACT90oGgi79BR3Svmhox9DI0xWXV5v-Thw/m=syvy,syvz,syvp,DhPYme,syy3,syxy,syy1,syy0,sywi,sywj,syxz,syxw,syxx,KHourd,MpJwZc,UUJqVe,sy7o,sOXFj,sy7n,s39S4,oGtAuc,NTMZac,nAFL3,sy81,sy80,q0xTif,y05UD,sy12k,sy192,syx4,sy18p,sy193,sy18w,syx3,syx2,syx1,sy18v,sy13u,sy18m,sy13y,sy18u,sy12g,sy18q,syh2,sy13z,sy18x,sy126,sy18t,sy18r,sy18s,sy18z,sy18h,sy18n,sy18g,sy18l,sy18i,sy18d,sy14u,sy141,sy142,syx9,syxa,epYOx?xjs=s3",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=1",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/md=2/k=xjs.hd.cs.-ck81h5K_qM.es5.O/am=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAACgAAAAAAQAAAAABAAAAAAAAAAEAQiAAAAgAAAEwAIAAAQDgAAAAAIAABABwKNsARAgAgAwAAAgAIAAwgIAABAAAAAIAAAEAAAAKAAAAAAACAAAAAAABAAAQIAAAAAAAAAAAAAAAQAA6AEAAAAAAAAABAQAAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/rs=ACT90oF2ZClyn8ynmeovVy8S38ywKiHRhw",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=4",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/client_204?atyp=i&biw=1176&bih=775&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&opi=89978449",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Priority": "u=5, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=csi&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&s=promo&rt=hpbas.1031&zx=1735503524027&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=i&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&dt19=3&prm23=0&zx=1735503524041&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/client_204?cs=2&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Pb5_UDKuMdBMkNmbreo2HiZQz6f_vNwu2Fr7b7JPXA3EP3VQhIU01wNOZ9SZh3FMtivqezohXpRNFZs7YHwqnQRWemE1hrlebcvAUE6eaJzeRPJdFzwC24YqyvpkWkvs8d9XeYx3b3YNQfe0RV4bRntLeyTsLmqrZUhsRn3JDgyax4LH8fHZEDTqbj-hPJUnkfsvy4inR0jGQTsD2kpdTMkaBFkLgiSzy1Duja9eyWKaaLnTRFoX",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/async/hpba?vet=10ahUKEwjnir645s2KAxWFBNsEHQX5CiYQj-0KCBU..i&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&opi=89978449&yv=3&sp_imghp=false&sp_hpte=1&sp_hpep=1&stick=&cs=0&async=_basejs:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.hd.cs.-ck81h5K_qM.es5.O%2Fam%3DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAACgAAAAAAQAAAAABAAAAAAAAAAEAQCAAAAgAAAEwAIAAAQDgAAAAAIAABABwKNsARAgAgAwAAAgAIAAwgIAABAAAAAIAAAEAAAAKAAAAAAACAAAAAAABAAAQIAAAAAAAAAAAAAAAQAA6AEAAAAAAAAABAQAAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg%2Fdg%3D0%2Fbr%3D1%2Frs%3DACT90oEHsB6dfTWSBhtYBSNqhvIua8mqsg,_basecss:%2Fxjs%2F_%2Fss%2Fk%3Dxjs.hd.1HG8niZTeao.L.F4.O%2Fam%3DCEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAAAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIAAgAwAgAMAAgAKAAAggRVAAgj4AAAlAAk98wGAAgEACAAIAAaUQUMgKgChABAAAAAAAABAAAAAQBAACAAAOgACwAAQCQCA6IEAAAAAAIIAAJATAJaBBwgAAAAAAACQAQAAAAwpIAAAAAAAAAAAAAAAAABEEAwFAAQEAAAAAAAAAAAAAAAAAACAQBME%2Fbr%3D1%2Frs%3DACT90oEuJKBfY6VuLOhgmh7m1ANPrbMj6g,_basecomb:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.hd.cs.-ck81h5K_qM.es5.O%2Fck%3Dxjs.hd.1HG8niZTeao.L.F4.O%2Fam%3DCEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAQAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIQDgAwAgAMAAhALwKNsgRVgAgj4AAAlAIk98wOAAhEACAAIAAaUQUMgKgChABAACAAAAABABAAAQJAACAAAOgACwAAQCQCA6IEAAAAAAIIABJQTAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg%2Fd%3D1%2Fed%3D1%2Fdg%3D0%2Fbr%3D1%2Fujg%3D1%2Frs%3DACT90oGgi79BR3Svmhox9DI0xWXV5v-Thw,_fmt:prog,_id:_pK5xZ-eoBoWJ7NYPhfKrsAI_8",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/gen_204?atyp=i&ct=psnt&cad=&nt=reload&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&zx=1735503524087&opi=89978449",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Priority": "u=5, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/k=xjs.hd.cs.-ck81h5K_qM.es5.O/ck=xjs.hd.1HG8niZTeao.L.F4.O/am=CEgVAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAICgAQEAwAQAdgEABAAAAABgAAAEAQiAAAAhBQAMwAIAAIQDgAwAgAMAAhALwKNsgRVgAgj4AAAlAIk98wOAAhEACAAIAAaUQUMgKgChABAACAAAAABABAAAQJAACAAAOgACwAAQCQCA6IEAAAAAAIIABJQTAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/d=0/dg=0/br=1/ujg=1/rs=ACT90oGgi79BR3Svmhox9DI0xWXV5v-Thw/m=sy1b7,P10Owf,sy19z,sy19x,sysj,gSZvdb,syyf,syye,WlNQGd,sysn,sysl,sysk,sysi,DPreE,syys,syyq,nabPbb,syy9,syy7,sylx,sypv,CnSW2d,kQvlef,syyr,fXO0xe?xjs=s3",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=i&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&vet=10ahUKEwjnir645s2KAxWFBNsEHQX5CiYQuqMJCIYB..s&bl=xroT&s=webhp&lpl=CAUQARgBMBE4A2IICAEQgJmkigE&zx=1735503524104&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=csi&ei=pa5xZ-GSG9fzi-gPxKC8uQs&s=async&astyp=hpba&ima=0&imn=0&hp=&rt=ttfb.279,st.282,bs.27,aaft.282,acrt.301,art.322&zx=1735503524353&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=csi&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&s=promo&rt=hpbas.1031,hpbarr.331&zx=1735503524357&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/xjs/_/js/k=xjs.hd.cs.-ck81h5K_qM.es5.O/am=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAACgAAAAAAQAAAAABAAAAAAAAAAEAQCAAAAgAAAEwAIAAAQDgAAAAAIAABABwKNsARAgAgAwAAAgAIAAwgIAABAAAAAIAAAEAAAAKAAAAAAACAAAAAAABAAAQIAAAAAAAAAAAAAAAQAA6AEAAAAAAAAABAQAAJaBBwgAAAAAAAD0AUDwAAwpLAAAAAAAAAAAAAAAAARMEMyFBAQEIAAAAAAAAAAAAAAAAACASBMXJg/d=0/dg=0/br=1/rs=ACT90oEHsB6dfTWSBhtYBSNqhvIua8mqsg/m=lOO0Vd,sy8i,P6sQOc?xjs=s4",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Priority": "u=1",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "play.google.com",
                "Connection": "keep-alive",
                "Content-Length": "1317",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "play.google.com",
                "Origin": "https://www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"cs",null,null,null,null,[1,0,0,0,0]]],373,[["1735503523623",null,null,null,null,null,null,"[1,40400,538,null,\\"706535361.0\\",\\"pK5xZ4SeB_bCxc8PqITR8Qs\\",null,null,null,\\"cs\\",\\"CZE\\",0,8,821,null,0,0,null,\\"og-40277818-b959-4db3-be14-5a2be13ab21d\\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,0,null,[2,5,\\"rd\\",28],null,null,0,0,1]",null,null,null,null,null,null,-3600,[null,null,null,"[null,null,[3701384]]"],null,null,null,null,1],["1735503524095",null,null,null,null,null,null,"[130,40400,538,null,\\"706535361.0\\",\\"pK5xZ4SeB_bCxc8PqITR8Qs\\",null,null,null,\\"cs\\",\\"CZE\\",0,8,1293,null,0,0,null,\\"og-40277818-b959-4db3-be14-5a2be13ab21d\\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,[2,5,\\"rd\\",28],null,null,0,0,1]",null,null,null,null,null,null,-3600,[null,null,null,"[null,null,[3701384]]"],null,null,null,null,2]],"1735503524644",null,null,null,null,null,null,null,null,null,null,null,null,null,[[null,[null,null,null,null,null,null,null,null,null,null,null,null,122505695]],9]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=csi&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&s=webhp&nt=reload&t=fi&st=10314&fid=12&zx=1735503533132&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?ei=pK5xZ-eoBoWJ7NYPhfKrsAI&ved=0ahUKEwjnir645s2KAxWFBNsEHQX5CiYQ4cIICIEB&uact=3&bl=xroT&s=webhp",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://consent.google.com/save?continue=https://www.google.com/&gl=CZ&m=0&pc=shp&x=5&src=2&hl=cs&bl=gws_20241211-0_RC2&uxe=none&cm=2&set_eom=true",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "consent.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=0",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?ei=pK5xZ-eoBoWJ7NYPhfKrsAI&vet=10ahUKEwjnir645s2KAxWFBNsEHQX5CiYQhJAHCCU..h&bl=xroT&s=webhp&cdot=9980",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/gen_204?atyp=i&ct=bxjs&cad=&b=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&zx=1735503533256&opi=89978449",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=0, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://ogs.google.com/widget/app/so?eom=1&awwd=1&origin=https%3A%2F%2Fwww.google.com&cn=app&pid=1&spid=538&hl=cs",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "ogs.google.com",
                "Priority": "u=4",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.cs.6Gopxdm2NFk.es5.O/am=gDAYcBs/d=1/excm=_b,_tp,appwidgetnoauthview/ed=1/dg=0/wt=2/ujg=1/rs=AM-SdHuhkWEEn8pbkl3UjmtGWNff6M0-ww/m=_b,_tp",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Priority": "u=2",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://ssl.gstatic.com/gb/images/sprites/p_2x_065643996766.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "ssl.gstatic.com",
                "Priority": "u=4, i",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/roboto/v18/KFOmCnqEu92Fr1Mu4mxK.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://ogs.google.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/roboto/v18/KFOmCnqEu92Fr1Mu7GxKOzY.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://ogs.google.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.cs.6Gopxdm2NFk.es5.O/ck=boq-one-google.OneGoogleWidgetUi.5A5oCTpuFxs.L.F4.O/am=gDAYcBs/d=1/exm=_b,_tp/excm=_b,_tp,appwidgetnoauthview/ed=1/wt=2/ujg=1/rs=AM-SdHsoH0g_h2pWt3lShNURWCDwDQ9vDA/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;ScI3Yc:e7Hzgb;Uvc8o:VDovNc;YIZmRd:A1yn5d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;dowIGb:ebZ3mb;eBAeSb:zbML3c;iFQyKf:QIhFr;lOO0Vd:OTA3Ae;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:MdUzUe;qafBPd:yDVVkb;qddgKe:xQtZb;wR5FRb:O1Gjze;xqZiqf:wmnU7d;yxTchf:KUM7Z;zxnPse:GkRiKb/m=ws9Tlc,n73qwf,GkRiKb,e5qFLc,IZT63,UUJqVe,O1Gjze,byfTOb,lsjVmc,xUdipf,ZDZcre,OTA3Ae,ZwDk9d,V3dDOb,mI3LFb,ORlaSe,O6y8ed,PrPYRd,MpJwZc,LEikZe,NwH0H,lazG7b,XVMNvd,L1AAkb,KUM7Z,s39S4,lwddkf,gychg,w9hDv,RMhBfe,SdcwHb,aW3pY,pw70Gc,EFQ78c,Ulmmrd,A7fCU,mdR7q,wmnU7d,xQtZb,JNoxi,MI6k7c,kjKdXe,BVgquf,QIhFr,hKSk3e,hc6Ubd,SpsfSb,Z5uLle,MdUzUe,zbML3c,zr1jrb,Uas9Hd,pjICDe",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.cs.6Gopxdm2NFk.es5.O/ck=boq-one-google.OneGoogleWidgetUi.5A5oCTpuFxs.L.F4.O/am=gDAYcBs/d=1/exm=A7fCU,BVgquf,EFQ78c,GkRiKb,IZT63,JNoxi,KUM7Z,L1AAkb,LEikZe,MI6k7c,MdUzUe,MpJwZc,NwH0H,O1Gjze,O6y8ed,ORlaSe,OTA3Ae,PrPYRd,QIhFr,RMhBfe,SdcwHb,SpsfSb,UUJqVe,Uas9Hd,Ulmmrd,V3dDOb,XVMNvd,Z5uLle,ZDZcre,ZwDk9d,_b,_tp,aW3pY,byfTOb,e5qFLc,gychg,hKSk3e,hc6Ubd,kjKdXe,lazG7b,lsjVmc,lwddkf,mI3LFb,mdR7q,n73qwf,pjICDe,pw70Gc,s39S4,w9hDv,wmnU7d,ws9Tlc,xQtZb,xUdipf,zbML3c,zr1jrb/excm=_b,_tp,appwidgetnoauthview/ed=1/wt=2/ujg=1/rs=AM-SdHsoH0g_h2pWt3lShNURWCDwDQ9vDA/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;ScI3Yc:e7Hzgb;Uvc8o:VDovNc;YIZmRd:A1yn5d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;dowIGb:ebZ3mb;eBAeSb:zbML3c;iFQyKf:QIhFr;lOO0Vd:OTA3Ae;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:MdUzUe;qafBPd:yDVVkb;qddgKe:xQtZb;wR5FRb:O1Gjze;xqZiqf:wmnU7d;yxTchf:KUM7Z;zxnPse:GkRiKb/m=p3hmRc,LvGhrf,RqjULd",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.cs.6Gopxdm2NFk.es5.O/ck=boq-one-google.OneGoogleWidgetUi.5A5oCTpuFxs.L.F4.O/am=gDAYcBs/d=1/exm=A7fCU,BVgquf,EFQ78c,GkRiKb,IZT63,JNoxi,KUM7Z,L1AAkb,LEikZe,LvGhrf,MI6k7c,MdUzUe,MpJwZc,NwH0H,O1Gjze,O6y8ed,ORlaSe,OTA3Ae,PrPYRd,QIhFr,RMhBfe,RqjULd,SdcwHb,SpsfSb,UUJqVe,Uas9Hd,Ulmmrd,V3dDOb,XVMNvd,Z5uLle,ZDZcre,ZwDk9d,_b,_tp,aW3pY,byfTOb,e5qFLc,gychg,hKSk3e,hc6Ubd,kjKdXe,lazG7b,lsjVmc,lwddkf,mI3LFb,mdR7q,n73qwf,p3hmRc,pjICDe,pw70Gc,s39S4,w9hDv,wmnU7d,ws9Tlc,xQtZb,xUdipf,zbML3c,zr1jrb/excm=_b,_tp,appwidgetnoauthview/ed=1/wt=2/ujg=1/rs=AM-SdHsoH0g_h2pWt3lShNURWCDwDQ9vDA/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;ScI3Yc:e7Hzgb;Uvc8o:VDovNc;YIZmRd:A1yn5d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;dowIGb:ebZ3mb;eBAeSb:zbML3c;iFQyKf:QIhFr;lOO0Vd:OTA3Ae;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:MdUzUe;qafBPd:yDVVkb;qddgKe:xQtZb;wR5FRb:O1Gjze;xqZiqf:wmnU7d;yxTchf:KUM7Z;zxnPse:GkRiKb/m=P6sQOc",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.cs.6Gopxdm2NFk.es5.O/ck=boq-one-google.OneGoogleWidgetUi.5A5oCTpuFxs.L.F4.O/am=gDAYcBs/d=1/exm=A7fCU,BVgquf,EFQ78c,GkRiKb,IZT63,JNoxi,KUM7Z,L1AAkb,LEikZe,LvGhrf,MI6k7c,MdUzUe,MpJwZc,NwH0H,O1Gjze,O6y8ed,ORlaSe,OTA3Ae,P6sQOc,PrPYRd,QIhFr,RMhBfe,RqjULd,SdcwHb,SpsfSb,UUJqVe,Uas9Hd,Ulmmrd,V3dDOb,XVMNvd,Z5uLle,ZDZcre,ZwDk9d,_b,_tp,aW3pY,byfTOb,e5qFLc,gychg,hKSk3e,hc6Ubd,kjKdXe,lazG7b,lsjVmc,lwddkf,mI3LFb,mdR7q,n73qwf,p3hmRc,pjICDe,pw70Gc,s39S4,w9hDv,wmnU7d,ws9Tlc,xQtZb,xUdipf,zbML3c,zr1jrb/excm=_b,_tp,appwidgetnoauthview/ed=1/wt=2/ujg=1/rs=AM-SdHsoH0g_h2pWt3lShNURWCDwDQ9vDA/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;ScI3Yc:e7Hzgb;Uvc8o:VDovNc;YIZmRd:A1yn5d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;dowIGb:ebZ3mb;eBAeSb:zbML3c;iFQyKf:QIhFr;lOO0Vd:OTA3Ae;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:MdUzUe;qafBPd:yDVVkb;qddgKe:xQtZb;wR5FRb:O1Gjze;xqZiqf:wmnU7d;yxTchf:KUM7Z;zxnPse:GkRiKb/m=Wt6vjf,hhhU8,FCpbqb,WhJNk",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Referer": "https://ogs.google.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "play.google.com",
                "Connection": "keep-alive",
                "Content-Length": "795",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "play.google.com",
                "Origin": "https://www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"cs",null,null,null,null,[1,0,0,0,0]]],373,[["1735503546341",null,null,null,null,null,null,"[144,40400,538,null,\\"706535361.0\\",\\"pK5xZ4SeB_bCxc8PqITR8Qs\\",null,null,null,\\"cs\\",\\"CZE\\",0,8,23539,null,0,0,null,\\"og-40277818-b959-4db3-be14-5a2be13ab21d\\",null,null,null,null,null,null,null,8,null,null,null,null,null,null,null,null,0,[1],3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,[2,5,\\"rd\\",28],null,null,0,0,1]",null,null,null,null,null,null,-3600,[null,null,null,"[null,null,[3701384]]"],null,null,null,null,3]],"1735503547344",null,null,null,null,null,null,null,null,null,null,null,null,null,[[null,[null,null,null,null,null,null,null,null,null,null,null,null,122505695]],9]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/gen_204?atyp=i&r=1&ei=pK5xZ-eoBoWJ7NYPhfKrsAI&ct=slh&v=t1&im=M&m=HV&pv=0.6028651190246667&me=1:1735503523306,V,0,0,1176,775:0,B,775:0,N,1,pK5xZ-eoBoWJ7NYPhfKrsAI:0,R,1,1,0,0,1176,775:740,x:9215,h,1,1,i:13074,h,1,1,o:8,h,1,1,i:45,h,1,1,o:6,h,1,1,i:8006,h,1,1,o:4,h,1,1,i:12989,G,1,1,380,749,1:0,c,380,749:0,G,1,1,380,749:5,e,C&zx=1735503567400&opi=89978449",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Origin": "https://www.google.com",
                "Priority": "u=6",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://google.com/search/howsearchworks/?fg=1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "google.com",
                "Priority": "u=0, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/?fg=1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=0, i",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.googleapis.com/css?family=Google+Sans+Display|Google+Sans:400,500|Google+Sans+Text:400,500&display=swap",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "fonts.googleapis.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.googleapis.com/icon?family=Material+Icons&display=swap",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "fonts.googleapis.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/main.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/js/main.min.js?fingerprint=dc331f54ec7d62fc91a56c1fd22086c9",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/header.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/images/icons/menu.svg?fingerprint=70797f2a4c042932241ad2f34e1c63e7",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/images/icons/menu_close.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/homepage-hero.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/image-with-text.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://lh3.googleusercontent.com/QTDlswXsuXqQRkS6wWKA_qstgp5KUEbl3zfVOhVKFJT19_iUlvvV_idYovHh6nDlzMttc-StGw2NzAplSxlWvR6C2UwXUDehIkv4xGs",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "lh3.googleusercontent.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/spacer.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/centered-video.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/footer.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://gstatic.com/images/branding/googlelogo/svg/googlelogo_dark54_clr_84x28px.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "gstatic.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesanstext/v22/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEp2iw.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesanstext/v22/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qER2i1dC.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvbQui-A3tw.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesanstext/v22/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmhjtg.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesanstext/v22/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmZjtiu7.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvbQui-A3tw.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjYUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjEUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjMUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjAUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiYUvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesans/v62/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj0UvbQui-A3t4TN.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesansdisplay/v21/ea8FacM9Wef3EJPWRrHjgE4B6CnlZxHVDv79oQ.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.gstatic.com/s/googlesansdisplay/v21/ea8FacM9Wef3EJPWRrHjgE4B6CnlZxHVDvD9oS_a.woff2",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "fonts.gstatic.com",
                "Origin": "https://www.google.com",
                "Referer": "https://fonts.googleapis.com/",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_dark54_clr_84x28px.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Priority": "u=5, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/searchbar-Intro-compressed_46432B98.mp4",
            headers={
                "Accept": "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=4",
                "Range": "bytes=0-",
                "Sec-Fetch-Dest": "video",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/hero-Loop-compressed_80CD2822.mp4",
            headers={
                "Accept": "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
                "Accept-Encoding": "identity",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=4",
                "Range": "bytes=0-",
                "Sec-Fetch-Dest": "video",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtm.js?id=GTM-WXBX8JC",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/config/2b.json?hl=cs",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Origin": "https://www.google.com",
                "Priority": "u=4",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/operating-anagram-8280/apple-touch-icon.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=6",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/operating-anagram-8280/favicon-16x16.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=6",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-JFPSXCWF8W&l=dataLayer&cx=c&gtm=45He4cc1v76610302za200",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.google-analytics.com/analytics.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "www.google-analytics.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://www.google-analytics.com/j/collect?v=1&_v=j101&a=1759635015&t=pageview&_s=1&dl=https%3A%2F%2Fwww.google.com%2Fsearch%2Fhowsearchworks%2F&dr=https%3A%2F%2Fwww.google.com%2F&ul=cs&de=UTF-8&dt=Vyhled%C3%A1v%C3%A1n%C3%AD%20Google%20%E2%80%93%20Jak%20Vyhled%C3%A1v%C3%A1n%C3%AD%20Google%20funguje&sd=24-bit&sr=1600x900&vp=1159x775&je=0&_u=YEBAAAABAAAAACgBI~&jid=903819329&gjid=797686753&cid=765093171.1735503570&tid=UA-96046856-1&_gid=1882063379.1735503570&_r=1&_slc=1&gtm=45He4cc1n81WXBX8JCv76610302za200&cd1=How%20Search%20Works&gcd=13l3l3l2l1l1&dma_cps=syphamo&dma=1&tag_exp=101925629~102067555~102067808~102081485~102198178&npa=1&z=915815104",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google-analytics.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain",
                "Host": "www.google-analytics.com",
                "Origin": "https://www.google.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/features/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "_ga_JFPSXCWF8W=GS1.1-3.1735503569.1.0.1735503569.0.0.0; _ga=GA1.1-3.765093171.1735503570; AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg; _ga=GA1.1.765093171.1735503570; _gid=GA1.1.1882063379.1735503570; _gat_UA-96046856-1=1",
                "Host": "www.google.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.googleapis.com/css?family=Google+Sans+Display|Google+Sans:400,500|Google+Sans+Text:400,500&display=swap",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "fonts.googleapis.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://fonts.googleapis.com/icon?family=Material+Icons&display=swap",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "fonts.googleapis.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/main.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.google.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/header.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.google.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/image-with-text.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.google.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/footer.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.google.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/images/icons/menu_close.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.google.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/js/main.min.js?fingerprint=dc331f54ec7d62fc91a56c1fd22086c9",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "_ga_JFPSXCWF8W=GS1.1-3.1735503569.1.1.1735503580.0.0.0; _ga=GA1.1-3.765093171.1735503570; AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg; _ga=GA1.1.765093171.1735503570; _gid=GA1.1.1882063379.1735503570; _gat_UA-96046856-1=1",
                "Host": "www.google.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search/howsearchworks/static/css/partials/primary-hero.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Cookie": "_ga_JFPSXCWF8W=GS1.1-3.1735503569.1.1.1735503580.0.0.0; _ga=GA1.1-3.765093171.1735503570; AEC=AZ6Zc-W7j8r5Ata4jiBc7Ay-wPOPFO5MKY4IhMXgnW0OWiyJOBXbpHAz1oE; __Secure-ENID=24.SE=Ne4cxC6IXVyoFuQVb2z2L79fEmiuWVFuEcMGQ2d-sodOeqqlxBpZvHB9ZbmieaS77FPQodWyVvoacZ7VSUZkgfp9Jlogzd31xLsRmWqdkPGqLo-CjS9VYn9TNJHdkMERdJwJhUG2XGbPn5l_DfKJtQ_zZZ4pYk8dfWTymya3haIPCi2fgJvoHPHR24F1v__5qNejkRWO7ZzsuDrXhBWX7fPFFqRAxtAZn5lHyT5LSMLYMo6_qGLiHNEMXJ8RJyk; SOCS=CAESHAgBEhJnd3NfMjAyNDEyMTEtMF9SQzIaAmNzIAEaBgiAosK7Bg; _ga=GA1.1.765093171.1735503570; _gid=GA1.1.1882063379.1735503570; _gat_UA-96046856-1=1",
                "Host": "www.google.com",
                "Priority": "u=2",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://lh3.googleusercontent.com/9IFxCJFBpUw9TIx58Q7VMQ5Kvbg-OFvIAx4_vya7PPAr9rjPnjKU7EUXq-9HOO-kkIScjJXYnWSzsy7ZfZVQZ6iZ-OmTu7emnlUhjQ",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "lh3.googleusercontent.com",
                "Connection": "keep-alive",
                "Host": "lh3.googleusercontent.com",
                "Priority": "u=4, i",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://gstatic.com/images/branding/googlelogo/svg/googlelogo_dark54_clr_84x28px.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "gstatic.com",
                "Connection": "keep-alive",
                "Host": "gstatic.com",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtm.js?id=GTM-WXBX8JC",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/googwebreview.appspot.com/grow-ext-cloud-images-uploads/features-Hero-compressed_F5521462.mp4",
            headers={
                "Accept": "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
                "Accept-Encoding": "identity",
                "Alt-Used": "storage.googleapis.com",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=4",
                "Range": "bytes=0-",
                "Sec-Fetch-Dest": "video",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "www.gstatic.com",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_dark54_clr_84x28px.svg",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.gstatic.com",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://www.gstatic.com/glue/cookienotificationbar/config/2b.json?hl=cs",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "www.gstatic.com",
                "Origin": "https://www.google.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-JFPSXCWF8W&l=dataLayer&cx=c&gtm=45He4cc1v76610302za200",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.google-analytics.com/analytics.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google-analytics.com",
                "Connection": "keep-alive",
                "Host": "www.google-analytics.com",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/operating-anagram-8280/apple-touch-icon.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "storage.googleapis.com",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=6",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://storage.googleapis.com/operating-anagram-8280/favicon-16x16.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "storage.googleapis.com",
                "Connection": "keep-alive",
                "Host": "storage.googleapis.com",
                "Priority": "u=6",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://www.google-analytics.com/j/collect?v=1&_v=j101&a=621603888&t=pageview&_s=1&dl=https%3A%2F%2Fwww.google.com%2Fsearch%2Fhowsearchworks%2Ffeatures%2F&ul=cs&de=UTF-8&dt=Funkce%20%E2%80%93%20Jak%20funguje%20Vyhled%C3%A1v%C3%A1n%C3%AD%20Google&sd=24-bit&sr=1600x900&vp=1159x775&je=0&_u=QAGAAAABAAAAACgBI~&jid=&gjid=&cid=765093171.1735503570&tid=UA-96046856-1&_gid=1882063379.1735503570&_slc=1&gtm=45He4cc1n81WXBX8JCv76610302za200&cd1=How%20Search%20Works&gcd=13l3l3l2l1l1&dma_cps=syphamo&dma=1&tag_exp=101925629~102067555~102067808~102081485~102198178&npa=1&z=552200766",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google-analytics.com",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Content-Type": "text/plain",
                "Host": "www.google-analytics.com",
                "Origin": "https://www.google.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(www_google_com)
