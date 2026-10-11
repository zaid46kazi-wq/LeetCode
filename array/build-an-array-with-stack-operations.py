class Solution:
    def buildArray(self, target, n):
        operations = []
        stream_number = 1
        target_index = 0
        
        while stream_number <= n and target_index < len(target):
            
            operations.append("Push")
            
            if stream_number == target[target_index]:
                target_index += 1
            else:
                operations.append("Pop")
            
            stream_number += 1
        
        return operations