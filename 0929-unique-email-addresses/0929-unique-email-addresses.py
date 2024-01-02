class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set=set()
        
        for email in emails:
            name,domain = email.split("@")
            if "+" in name:
                name=name[:name.index("+")]
            name=name.replace(".","")
            hash_set.add(name + "@" + domain)
            
            
        return len(hash_set)