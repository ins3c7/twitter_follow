elm=bro.find_elements(By.XPATH, '//span[@class="button-text follow-text"]');print str(len(elm)), 'carregados...';x=0;random.shuffle(elm);e=0;c=0

for el in elm:
  try:
    el.click()
    time.sleep(float(str(random.randrange(2,4))+'.'+str(random.randrange(90))))
    print '[+]',len(elm)-x;x+=1;c+=1
  except:
    print '[-]',len(elm)-x;x+=1;e+=1
    pass

print '\nerros:',str(e),'\ncompletos:',str(c)
print
