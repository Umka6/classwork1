# name = 'Tramp'
# lastname = 'Donald'
# time = 17.7
#
# sms = 'Пропущенных вызовов от {n} {l} в {t} .Для прослушивания сообщений, пожалуйста, наберите *790.'.format(n=name,l=lastname,t=time)
#
# print(sms)
# #Пропущенных вызовов от Ивана Сергеича в 16:27: 1,
# #Для прослушивания сообщений, пожалуйста, наберите *790

name = ['Turat','Aito','Kirill','Taalai','Umut','Adelina']

s = 'привет! {0[0]} \nкак дела? {0[1]} \nbonjur! {0[2]}\nhow are you? {0[3]}\nmerci: {0[4]}\nhi: {0[5]}'.format(name)
print(s)
