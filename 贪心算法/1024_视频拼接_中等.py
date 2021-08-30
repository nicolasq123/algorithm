class Solution:
    def videoStitching(self, clips, time):
        """
        1. start顺序，end逆序。 clips[n][0] <= clips[n+1][0].
        2. 示意图如下
------
 ----
  --
   ----

        3. 需要需要的片段数, return -1 if cannot
        4. 初始不为0，return-1； 当覆盖的区间>=time,break;
        """

        def cmp(item):
            return (item[0], -item[1])
        clips.sort(key=cmp)
        print(clips)

        if time == 0:
            return 0
        if len(clips) == 0:
            return -1
        if clips[0][0] != 0:
            return -1

        ok = False
        nums = 1 # 需要的

        start = 0 #当前被比较的index
        i = 1

        obs = [clips[0]]
        while i < len(clips):
            if obs[-1][1] >= time:
                break

            if clips[i][0] > clips[start][1]:
                print(clips[i], clips[start])
                return -1 # 出现空隙

            if clips[i][1] >= clips[start][1]:
                j = i
                idx = i
                maxend = clips[i][1]
                while j < len(clips) and clips[j][0] <= clips[start][1]:
                    if clips[j][1] > maxend:
                        idx = j
                        maxend = clips[j][1]
                    j += 1
                start = idx
                obs.append(clips[start])
                i = j-1
                nums += 1
                print("----------", start, i, nums)

            else : # clips[i][1] < clips[start][1]:
                pass
            i += 1

        print("----------obs", obs)
        if obs[-1][1] < time:
            print("------last < time", obs[-1][1])
            return -1
        return nums

if __name__ == '__main__':
    print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))