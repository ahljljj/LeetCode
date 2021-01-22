# 838. Push Dominoes

# 2021/01/21, two pointer


# 注意：这题就是普通的循环，理解了很容易写出来。
# 将dominoes根据"R"或"L"分成数个小段
# 1、L..L, R..R这段所有的都会变为L或R; 2、L...R这段保持不变
# 3、R...L前半段变为R，后半段变为L
# 细节很多，想要完整正确的写出来不是很容易。




class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = ""
        cuts = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        cuts = [(-1, "L")] + cuts + [(len(dominoes), "R")]
        for k in range(1, len(cuts)):
            i, state = cuts[k][0], cuts[k][1]
            prev_i, prev_state = cuts[k - 1][0], cuts[k - 1][1]
            if prev_i != -1: ans += prev_state
            if state == prev_state:
                ans += state * ( (i - 1) - (prev_i + 1) + 1 )
            elif prev_state > state:
                d = ( (i - 1) - (prev_i + 1) + 1)
                if d % 2 == 0:
                    ans += prev_state * (d // 2) + state * (d // 2)
                else:
                    ans += prev_state * (d // 2) + "." + state * (d // 2)
            else:
                ans += "." * ( (i - 1) - (prev_i + 1) + 1 )
        return ans