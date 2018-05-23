# Author:zhang
# -*- coding:utf-8 -*-

import requests
def kk(title,content):
    url2 = "https://passport.cnblogs.com/user/signin"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
    s = requests.session()
    # 获取登录之前的cookies
    s.get(url=url2, headers=headers, verify=False)
    print(s.cookies)

    # 添加登录需要的cookie:.往session里面添加cookie
    c = requests.cookies.RequestsCookieJar()
    a="3335B0C4E81E225BA2B00BFE37AB33008BC8991A75501B96FFD051228AF0AEA6676617C264A4C876F70C3449750DD58B742C7805E78D07374D4D75FAC3DD1E68D9A8880BB57B9D67DDEE3A1DDBFF12DFC898626F"
    b="CfDJ8Gf3jjv4cttDnEy2UYRcGZ3faejWTW1-yD_wNAeth7JzsZ5ESons0j3LdgshUfeH8a5YGFuP-dob35HFouRZ5Cd6kxIp2-e2HUWZ7-MuLazzJAd6M4JjhdAyDbI19s5fsSc5iin4FjhlaFss45ETe0lQkYJbPdHYzw7M6pQ0WcNTjsp7PMVdOq-opRdzKG1d_1G2Itxou7LiUJeTTmKaaeAhf1dbLAFHF4AW_1dy9R_vSJqvgyu9X1PyJV49D4LKhxdYG4tFTGFBdQTzFZxbeM0nm2rhkJGbzj_5OhqtbZWp"
    c.set('.CNBlogsCookie', a)
    c.set('.Cnblogs.AspNetCore.Cookies', b)
    c.set('AlwaysCreateItemsAsActive', "True")
    c.set('AdminCookieAlwaysExpandAdvanced', "True")
    s.cookies.update(c)
    #草稿的body
    # body = {"__VIEWSTATE": "",
    #         "__VIEWSTATEGENERATOR": "FE27D343",
    #         "Editor$Edit$txbTitle": title,
    #         "Editor$Edit$EditorBody": "<p>"+content+"</p>",
    #         "Editor$Edit$Advanced$ckbPublished": "on",
    #         "Editor$Edit$Advanced$chkDisplayHomePage": "on",
    #         "Editor$Edit$Advanced$chkComments": "on",
    #         "Editor$Edit$Advanced$chkMainSyndication": "on",
    #         "Editor$Edit$Advanced$txbEntryName": "",
    #         "Editor$Edit$Advanced$txbExcerpt": "",
    #         "Editor$Edit$Advanced$txbTag": "",
    #         "Editor$Edit$Advanced$tbEnryPassword": "",
    #         "Editor$Edit$lkbDraft": "存为草稿"}
    # 发布的body
    body1={"Editor$Edit$EditorBody":	"<p>"+content+"</p>",
        "Editor$Edit$lkbPost":	"发布",
        "Editor$Edit$Advanced$chkComments":	"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":	"on",

        "Editor$Edit$Advanced$ckbPublished":	"on",
        "Editor$Edit$txbTitle":	title,
        "__VIEWSTATEGENERATOR":	"FE27D343",

        "Editor$Edit$Advanced$chkMainSyndication":	"on",
           "__VIEWSTATE":"",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$txbTag":""	,
        "Editor$Edit$Advanced$tbEnryPassword":""}

    # s=requests.session()

    # r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
    url3 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    # @直接进行了编辑
    r2 = s.post(url3, data=body1, verify=False)
    print(r2.content)
kk("titleya","english")



def aaaa():
    content="""class cnbl_login():
        def __init__(self, title, content):
            self.title = title
            self.content = content

        def obtain_cookie(self):
            url2 = "https://passport.cnblogs.com/user/signin"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
            s = requests.session()
            # 获取登录之前的cookies
            s.get(url=url2, headers=headers, verify=False)
            "向session添加cookie"
            c = requests.cookies.RequestsCookieJar()
            a = "9CDE56DF811CC8E1C8E121991D18645E36FFB73FC988A2BB56BEB5C412A3BF62E8268F9DEE9789DF245A9A6A4E32008B7026D9BADB9EEF789121510E07BCCD5B964C918BD2155A8B88C58677C568AC8CCBC59EF7"
            b = "CfDJ8Gf3jjv4cttDnEy2UYRcGZ0FTklmBazTAlRQiOmC-I8priUt__x2Sm_RKXQHmoYS1FYOUd5OFwsCaje5QLtrfxlQ-NFNwOqC2KJ246crqLvgowAk-EbisMavvaFxDU7-OEgM8XY9OHShjTKXNCzUanwqY5NKl8BS1-Sip_TIsw_OGaH-zoEFui0s3_10Di-jILkA96Cqe-6a_vnyxI68hFF9Q8mHJzrvhfflgSWgbDPPqyBmaoGQ8W7yKvWXIHk5K72WRuZmpRaMyvAElyuVRK_0feKRg8SS7Z3wz1J0-gWf"
            c.set('.CNBlogsCookie', a)
            c.set('.Cnblogs.AspNetCore.Cookies', b)
            c.set('AlwaysCreateItemsAsActive', "True")
            c.set('AdminCookieAlwaysExpandAdvanced', "True")
            s.cookies.update(c)

        def savve_draft(self):

            "保存草稿"
            body = {"__VIEWSTATE": "",
                    "__VIEWSTATEGENERATOR": "FE27D343",
                    "Editor$Edit$txbTitle": self.title,
                    "Editor$Edit$EditorBody": "<p>" + self.content + "</p>",
                    "Editor$Edit$Advanced$ckbPublished": "on",
                    "Editor$Edit$Advanced$chkDisplayHomePage": "on",
                    "Editor$Edit$Advanced$chkComments": "on",
                    "Editor$Edit$Advanced$chkMainSyndication": "on",
                    "Editor$Edit$Advanced$txbEntryName": "",
                    "Editor$Edit$Advanced$txbExcerpt": "",
                    "Editor$Edit$Advanced$txbTag": "",
                    "Editor$Edit$Advanced$tbEnryPassword": "",
                    "Editor$Edit$lkbDraft": "存为草稿"}
            url3 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
            # @直接进行了编辑
            r2 = s.post(url3, data=body, verify=False)
            print(r2.content)

    if __name__ == '__main__':
        login=cnbl_login("country","qiang")
        login.obtain_cookie()
        login.savve_draft()"""
