print('TASK 1')
while True:
    print('Type 00 if you wanna end this programme)')
    a = int(input('Number in range 0-99: ')) 
    if a == 00:
        break
    else:
        def num():
            def numssss(w):
                if w == 0:
                    return ''
                if w == 1:
                    return 'one'
                if w == 2:
                    return 'two'
                if w == 3:
                    return 'three'
                if w == 4:
                    return 'four'
                if w == 5:
                    return 'five'
                if w == 6:
                    return 'six'
                if w == 7:
                    return 'seven'
                if w == 8:
                    return 'eight'
                if w == 9:
                    return 'nine'
            x = a % 10
            if a in range(0, 100):
                if a in range(1, 10):
                    return numssss(a)
                if a == 0:
                    return 'zero'
                if a in range(10, 20):
                    if a == 10:
                        return 'ten'
                    if a == 11:
                        return 'eleven'
                    if a == 12:
                        return 'twelve'
                    if a == 13:
                        return 'thirteen'
                    if a in range(14, 20):
                        return f'{numssss(x)}teen'
                if a in range(20, 30):
                    return f'twenty-{numssss(x)}'
                if a in range(30, 40):
                    return f'thirty-{numssss(x)}'
                if a in range(40, 50):
                    return f'fourty-{numssss(x)}'
                if a in range(50, 60):
                    return f'fifty-{numssss(x)}'        
                if a in range(60, 70):
                    return f'sixty-{numssss(x)}'    
                if a in range(70, 80):
                    return f'seventy-{numssss(x)}'     
                if a in range(80, 90):
                    return f'eighty-{numssss(x)}'  
                if a in range(90, 100):
                    return f'ninety-{numssss(x)}'     
            else:
                print('Type Error!')
        print(num())
print()

print('TASK 2')
while True:
    print('If you wanna stop this programme, type 00)')
    s = input('stdin:')      
    d = s.capitalize()
    if d == '00':
        break
    else:
        def months(ss):
            if ss == 'Jan':
                return f'stdout:1'
            elif ss == 'Feb':
                return f'stdout:2'
            elif ss == 'Mar':
                return f'stdout:3'
            elif ss == 'Apr':
                return f'stdout:4'
            elif ss == 'May':
                return f'stdout:5'
            elif ss == 'Jun':
                return f'stdout:6'
            elif ss == 'Jul':
                return f'stdout:7'
            elif ss == 'Aug':
                return f'stdout:8'
            elif ss == 'Sep':
                return f'stdout:9'
            elif ss == 'Oct':
                return f'stdout:10'
            elif ss == 'Nov':
                return f'stdout:11'
            elif ss == 'Dec':
                return f'stdout:12'
            else:
                print('TypeError!')
        print(months(d))
print()