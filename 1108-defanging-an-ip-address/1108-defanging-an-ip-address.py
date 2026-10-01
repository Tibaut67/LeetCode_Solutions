class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_text = address.replace(".", "[.]")
        return new_text