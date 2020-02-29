class cron:
    def limp(self):
        #cronサンプル
        f = open('./sample.text')
        x =f.read()
        f.close()
        x = x + "a"
        f = open('./sample.text','w')
        f.writelines(x)
        f.close()
        f = open('./sample.text')
        text =f.read()
        f.close()
        return text