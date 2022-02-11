from string import ascii_lowercase, digits
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        stack = []
        string = ''
        reps = ''
        while i < len(s):
            c = s[i]

            if c in digits:
                reps += c


            elif c in ascii_lowercase:
                string += c

            elif c  == '[':

                stack.append(int(reps))
                reps = ''

            elif c == ']':
                num = stack.pop()
                string = string * num
                stack.append(string)

                string = ''


            i += 1
        return ''.join(stack)

class Solution2:
    def decodeString(self, s : str):
        n = len(s)
        i = 0
        nums_stack = []
        char_stack = []
        num = ''
        string = ''

        while i < n:
            c = s[i]

            if c in digits:
                num += c
                if string:
                    char_stack.append(string)
                    string = ''
            elif c in ascii_lowercase:
                string += c

            elif c == '[':
                if num:
                    nums_stack.append(int(num))
                    num = ''
                char_stack.append(c)

            else:
                if string:
                    char_stack.append(string)
                    string = ''
                numm = nums_stack.pop()
                ss = ''
                tc = char_stack.pop()
                while tc != '[':
                    ss = tc + ss
                    tc = char_stack.pop()


                char_stack.append(ss * numm)

            i += 1


        if string:
            char_stack.append(string)
        return ''.join(char_stack)



    def superDigit(self,n,k):
        def sd(n):
            if n < 10:
                return n
            digits = []
            while n:
                n, d = divmod(n,10)
                digits.append(d)

            return sd(sum(digits))

        digits = []
        while n:
            n, d = divmod(n,10)
            digits.append(d)
        return sd(sum(digits) * k)





if __name__ == '__main__':
    print(Solution2().decodeString(s = "3[a2[c]]"))
    print(Solution2().decodeString(s = "3[a]2[bc]"))
    print(Solution2().decodeString(s="2[abc]3[cd]ef"))
    # print(Solution2().superDigit(7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153,100000))
    # print(Solution2().superDigit(148,3))