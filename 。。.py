# import requests
# from bs4 import BeautifulSoup
#
# headers={'。。。。。。'}
#
#
# for i in range(3):
#     url = 'https://www.jobui.com/company/16235804/jobs/p{x}/'
#     real_url = url.format(x =i+1)
#
#     print("__________")
#     print('第'+ str(i+1) +'页')
#     res = requests.get(real_url,headers = headers)
#     soup = BeautifulSoup(res.text,'html.parser')
#     items = soup.find_all(class_ = 'c-job-list')
# 
#     for item in items:
#         company_name = item.find(class_ = 'job-name').find('h3')
#         company_location = item.find('span')
#         academic = item.find('span').next_sibling.next_sibling.next_sibling.next_sibling
#         print(company_name.text,company_location.text,academic.text)
#     print("__________")