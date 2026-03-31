class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        insert = 0

        while right < len(chars):
            temp = chars[left]

            count = 0

            while right < len(chars) and temp == chars[right]:
                count += 1
                right += 1
            
            chars[insert] = temp
            insert += 1

            if count >1:
                count = str(count)
                for c in count:
                    chars[insert] = c
                    insert += 1
                
            left = right
        
        return insert