while 1:
    s = raw_input().strip()
    if s != '':
        jd = s.split()
        num = int(jd[0])
        w = int(jd[1])
        h = int(jd[2])
        envs = []
        res = 0
        for i in range(num):
            env = raw_input().strip().split()
            env = [int(k) for k in env]
            if env[0] > w and env[1] > h:
                env.append(i+1)
                envs.append(env)
    
        envs = sorted(envs)
        #print envs

        for i in range(len(envs)):
            if envs[i][2] == '':
                pass
            else:
                for j in range(i+1,len(envs)):
                    if envs[i][0] < envs[j][0] and envs[i][1] < envs[j][1]:
                        pass
                    else:
                        envs[j][2] = ''
            
        #print(envs)
        #print dis
        dis = 0
        for env in envs:
            dis += env.count('') 
        print(len(envs) - dis)
        for i in range(len(envs)):
            if envs[i][2] != '':
                print envs[i][2],
            if i == len(envs) - 1:
                print ''
    else:
        break



    
