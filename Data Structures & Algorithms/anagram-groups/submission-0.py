class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_list = {}
        for c_sub in strs:
            check_sub = list(c_sub)
            check_sub.sort()
            check_sub = str(check_sub)
            to_add = list()
            if check_sub not in res_list:
                 res_list[check_sub] = to_add
            res_list[check_sub].append(c_sub)

        res = []
        for i in res_list.values():
            res.append(i)
        return res