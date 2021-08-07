# -*- coding: utf-8 -*-
import json
'''
To make CGV Thaeter lists
{
    "01": [
        {
            "TheaterCode": "0056",
            "TheaterName": "CGV\uac15\ub0a8"
        },
        {
            "TheaterCode": "0001",
            "TheaterName": "CGV\uac15\ubcc0"
        },
        ],
    "02": [
        ...
        ],
    ...
}
    
'''

data = {}

AreaTheaterDetailList1 = '{"AreaTheaterDetailList":[{"RegionCode":"01","TheaterCode":"0056","TheaterName":"CGV강남","TheaterName_ENG":null,"IsSelected":true},{"RegionCode":"01","TheaterCode":"0001","TheaterName":"CGV강변","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0229","TheaterName":"CGV건대입구","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0010","TheaterName":"CGV구로","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0063","TheaterName":"CGV대학로","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0252","TheaterName":"CGV동대문","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0230","TheaterName":"CGV등촌","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0009","TheaterName":"CGV명동","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0105","TheaterName":"CGV명동역 씨네라이브러리","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0011","TheaterName":"CGV목동","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0057","TheaterName":"CGV미아","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0030","TheaterName":"CGV불광","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0046","TheaterName":"CGV상봉","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0300","TheaterName":"CGV성신여대입구","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0088","TheaterName":"CGV송파","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0276","TheaterName":"CGV수유","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0150","TheaterName":"CGV신촌아트레온","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0040","TheaterName":"CGV압구정","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0112","TheaterName":"CGV여의도","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0292","TheaterName":"CGV연남","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0059","TheaterName":"CGV영등포","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0074","TheaterName":"CGV왕십리","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0013","TheaterName":"CGV용산아이파크몰","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0131","TheaterName":"CGV중계","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0199","TheaterName":"CGV천호","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0107","TheaterName":"CGV청담씨네시티","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0223","TheaterName":"CGV피카디리1958","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0164","TheaterName":"CGV하계","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"0191","TheaterName":"CGV홍대","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"P001","TheaterName":"CINE de CHEF 압구정","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"01","TheaterCode":"P013","TheaterName":"CINE de CHEF 용산아이파크몰","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"01","RegionName":"서울","RegionName_ENG":"","DisplayOrder":"1","IsSelected":true}'
AreaTheaterDetailList2 = '{"AreaTheaterDetailList":[{"RegionCode":"02","TheaterCode":"0260","TheaterName":"CGV경기광주","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0255","TheaterName":"CGV고양행신","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0257","TheaterName":"CGV광교","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0266","TheaterName":"CGV광교상현","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0232","TheaterName":"CGV구리","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0278","TheaterName":"CGV김포","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0188","TheaterName":"CGV김포운양","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0126","TheaterName":"CGV김포풍무","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0298","TheaterName":"CGV김포한강","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0124","TheaterName":"CGV동백","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0041","TheaterName":"CGV동수원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0106","TheaterName":"CGV동탄","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0265","TheaterName":"CGV동탄역","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0233","TheaterName":"CGV동탄호수공원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0226","TheaterName":"CGV배곧","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0155","TheaterName":"CGV범계","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0015","TheaterName":"CGV부천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0194","TheaterName":"CGV부천역","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0287","TheaterName":"CGV부천옥길","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0049","TheaterName":"CGV북수원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0242","TheaterName":"CGV산본","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0196","TheaterName":"CGV서현","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0304","TheaterName":"CGV성남모란","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0143","TheaterName":"CGV소풍","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0012","TheaterName":"CGV수원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0274","TheaterName":"CGV스타필드시티위례","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0073","TheaterName":"CGV시흥","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0211","TheaterName":"CGV안산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0279","TheaterName":"CGV안성","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0003","TheaterName":"CGV야탑","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0262","TheaterName":"CGV양주옥정","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0338","TheaterName":"CGV역곡","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0004","TheaterName":"CGV오리","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0305","TheaterName":"CGV오산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0307","TheaterName":"CGV오산중앙","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0271","TheaterName":"CGV용인","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0113","TheaterName":"CGV의정부","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0187","TheaterName":"CGV의정부태흥","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0205","TheaterName":"CGV이천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0054","TheaterName":"CGV일산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0320","TheaterName":"CGV정왕","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0055","TheaterName":"CGV죽전","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0148","TheaterName":"CGV파주문산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0310","TheaterName":"CGV파주야당","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0181","TheaterName":"CGV판교","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0195","TheaterName":"CGV평촌","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0052","TheaterName":"CGV평택","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0214","TheaterName":"CGV평택소사","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0309","TheaterName":"CGV포천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0326","TheaterName":"CGV하남미사","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0301","TheaterName":"CGV화성봉담","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"02","TheaterCode":"0145","TheaterName":"CGV화정","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"02","RegionName":"경기","RegionName_ENG":"","DisplayOrder":"2","IsSelected":false}'
AreaTheaterDetailList3 = '{"AreaTheaterDetailList":[{"RegionCode":"202","TheaterCode":"0043","TheaterName":"CGV계양","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0198","TheaterName":"CGV남주안","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0021","TheaterName":"CGV부평","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0325","TheaterName":"CGV송도타임스페이스","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0247","TheaterName":"CGV연수역","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0002","TheaterName":"CGV인천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0118","TheaterName":"CGV인천공항","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0254","TheaterName":"CGV인천논현","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0340","TheaterName":"CGV인천도화","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0258","TheaterName":"CGV인천연수","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0269","TheaterName":"CGV인천학익","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0308","TheaterName":"CGV주안역","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0235","TheaterName":"CGV청라","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"202","TheaterCode":"0339","TheaterName":"DRIVE IN 스퀘어원","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"202","RegionName":"인천","RegionName_ENG":"","DisplayOrder":"3","IsSelected":false}'
AreaTheaterDetailList4 = '{"AreaTheaterDetailList":[{"RegionCode":"12","TheaterCode":"0139","TheaterName":"CGV강릉","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"12","TheaterCode":"0144","TheaterName":"CGV원주","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"12","TheaterCode":"0281","TheaterName":"CGV인제","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"12","TheaterCode":"0070","TheaterName":"CGV춘천","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"12","RegionName":"강원","RegionName_ENG":"","DisplayOrder":"4","IsSelected":false}'
AreaTheaterDetailList5 = '{"AreaTheaterDetailList":[{"RegionCode":"205","TheaterCode":"0261","TheaterName":"CGV논산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0207","TheaterName":"CGV당진","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0007","TheaterName":"CGV대전","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0286","TheaterName":"CGV대전가수원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0154","TheaterName":"CGV대전가오","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0202","TheaterName":"CGV대전탄방","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0127","TheaterName":"CGV대전터미널","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0275","TheaterName":"CGV보령","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0091","TheaterName":"CGV서산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0219","TheaterName":"CGV세종","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"03","TheaterCode":"0206","TheaterName":"CGV유성노은","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0044","TheaterName":"CGV천안","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0332","TheaterName":"CGV천안시청","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0293","TheaterName":"CGV천안터미널","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0110","TheaterName":"CGV천안펜타포트","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0228","TheaterName":"CGV청주(서문)","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0297","TheaterName":"CGV청주성안길","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0282","TheaterName":"CGV청주율량","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0142","TheaterName":"CGV청주지웰시티","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0319","TheaterName":"CGV청주터미널","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0284","TheaterName":"CGV충북혁신","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0328","TheaterName":"CGV충주교현","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"205","TheaterCode":"0217","TheaterName":"CGV홍성","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"03,205","RegionName":"대전/충청","RegionName_ENG":"","DisplayOrder":"5","IsSelected":false}'
AreaTheaterDetailList6 = '{"AreaTheaterDetailList":[{"RegionCode":"11","TheaterCode":"0058","TheaterName":"CGV대구","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0157","TheaterName":"CGV대구수성","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0108","TheaterName":"CGV대구스타디움","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0185","TheaterName":"CGV대구아카데미","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0216","TheaterName":"CGV대구월성","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0117","TheaterName":"CGV대구이시아","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0071","TheaterName":"CGV대구칠곡","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0147","TheaterName":"CGV대구한일","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"11","TheaterCode":"0109","TheaterName":"CGV대구현대","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"11","RegionName":"대구","RegionName_ENG":"","DisplayOrder":"6","IsSelected":false}'
AreaTheaterDetailList7 = '{"AreaTheaterDetailList":[{"RegionCode":"05","TheaterCode":"0065","TheaterName":"CGV남포","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0061","TheaterName":"CGV대연","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0042","TheaterName":"CGV동래","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0005","TheaterName":"CGV서면","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0285","TheaterName":"CGV서면삼정타워","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0089","TheaterName":"CGV센텀시티","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0160","TheaterName":"CGV아시아드","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"207","TheaterCode":"0128","TheaterName":"CGV울산삼산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"207","TheaterCode":"0264","TheaterName":"CGV울산신천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"207","TheaterCode":"0246","TheaterName":"CGV울산진장","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0306","TheaterName":"CGV정관","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0245","TheaterName":"CGV하단아트몰링","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0318","TheaterName":"CGV해운대","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"0159","TheaterName":"CGV화명","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"05","TheaterCode":"P004","TheaterName":"CINE de CHEF 센텀","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"05,207","RegionName":"부산/울산","RegionName_ENG":"","DisplayOrder":"7","IsSelected":false}'
AreaTheaterDetailList8 = '{"AreaTheaterDetailList":[{"RegionCode":"204","TheaterCode":"0263","TheaterName":"CGV거제","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0330","TheaterName":"CGV경산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0323","TheaterName":"CGV고성","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0053","TheaterName":"CGV구미","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0240","TheaterName":"CGV김천율곡","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0028","TheaterName":"CGV김해","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0311","TheaterName":"CGV김해율하","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0239","TheaterName":"CGV김해장유","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0033","TheaterName":"CGV마산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0097","TheaterName":"CGV북포항","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0272","TheaterName":"CGV안동","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0222","TheaterName":"CGV양산물금","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0234","TheaterName":"CGV양산삼호","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0324","TheaterName":"CGV진주혁신","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0023","TheaterName":"CGV창원","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0079","TheaterName":"CGV창원더시티","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0283","TheaterName":"CGV창원상남","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0156","TheaterName":"CGV통영","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"204","TheaterCode":"0045","TheaterName":"CGV포항","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"204","RegionName":"경상","RegionName_ENG":"","DisplayOrder":"8","IsSelected":false}'
AreaTheaterDetailList9 = '{"AreaTheaterDetailList":[{"RegionCode":"04","TheaterCode":"0220","TheaterName":"CGV광양","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0221","TheaterName":"CGV광양 엘에프스퀘어","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0295","TheaterName":"CGV광주금남로","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0193","TheaterName":"CGV광주상무","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0210","TheaterName":"CGV광주용봉","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0218","TheaterName":"CGV광주첨단","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0244","TheaterName":"CGV광주충장로","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0090","TheaterName":"CGV광주터미널","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"206","TheaterCode":"0215","TheaterName":"CGV광주하남","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0277","TheaterName":"CGV군산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0237","TheaterName":"CGV나주","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0289","TheaterName":"CGV목포","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0280","TheaterName":"CGV목포평화광장","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0225","TheaterName":"CGV서전주","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0114","TheaterName":"CGV순천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0268","TheaterName":"CGV순천신대","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0315","TheaterName":"CGV여수웅천","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0020","TheaterName":"CGV익산","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0213","TheaterName":"CGV전주고사","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0179","TheaterName":"CGV전주효자","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"04","TheaterCode":"0186","TheaterName":"CGV정읍","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"06","TheaterCode":"0302","TheaterName":"CGV제주","TheaterName_ENG":null,"IsSelected":false},{"RegionCode":"06","TheaterCode":"0259","TheaterName":"CGV제주노형","TheaterName_ENG":null,"IsSelected":false}],"RegionCode":"206,04,06","RegionName":"광주/전라/제주","RegionName_ENG":"","DisplayOrder":"9","IsSelected":false}'

AreaTheaterDetailList1 = json.loads(AreaTheaterDetailList1)
AreaTheaterDetailList2 = json.loads(AreaTheaterDetailList2)
AreaTheaterDetailList3 = json.loads(AreaTheaterDetailList3)
AreaTheaterDetailList4 = json.loads(AreaTheaterDetailList4)
AreaTheaterDetailList5 = json.loads(AreaTheaterDetailList5)
AreaTheaterDetailList6 = json.loads(AreaTheaterDetailList6)
AreaTheaterDetailList7 = json.loads(AreaTheaterDetailList7)
AreaTheaterDetailList8 = json.loads(AreaTheaterDetailList8)
AreaTheaterDetailList9 = json.loads(AreaTheaterDetailList9)

Area1 = AreaTheaterDetailList1.get('AreaTheaterDetailList')
Area2 = AreaTheaterDetailList2.get('AreaTheaterDetailList')
Area3 = AreaTheaterDetailList3.get('AreaTheaterDetailList')
Area4 = AreaTheaterDetailList4.get('AreaTheaterDetailList')
Area5 = AreaTheaterDetailList5.get('AreaTheaterDetailList')
Area6 = AreaTheaterDetailList6.get('AreaTheaterDetailList')
Area7 = AreaTheaterDetailList7.get('AreaTheaterDetailList')
Area8 = AreaTheaterDetailList8.get('AreaTheaterDetailList')
Area9 = AreaTheaterDetailList9.get('AreaTheaterDetailList')

Areas = [Area1, Area2, Area3, Area4, Area5, Area6, Area7, Area8, Area9]

data['01'] = []
data['02'] = []
data['03'] = []
data['04'] = []
data['05'] = []
data['06'] = []
data['11'] = []
data['12'] = []
data['202'] = []
data['204'] = []
data['205'] = []
data['206'] = []
data['207'] = []


for Area in Areas:
  for theater in Area:
    print(theater)
    RegionCode = theater['RegionCode']
    TheaterCode = theater['TheaterCode']
    TheaterName = theater['TheaterName']
    print(f"RegionCode: {RegionCode}, TheaterCode: {TheaterCode}, TheaterName: {TheaterName}")
    data[RegionCode].append({'TheaterCode': TheaterCode, 'TheaterName': TheaterName})

print(data)

with open('../theater/data/AreaCodes.json', 'w') as outfile:
  json.dump(data, outfile, indent=4)
