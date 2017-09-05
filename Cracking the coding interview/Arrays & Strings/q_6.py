'''
Problem: String Compression
Description: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Solved: True
'''

def compress_string(s):
    count = 1
    track = [s[0]]

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            track.append(str(count))
            track.append(s[i])
            count = 1

    track.append(str(count))
    return ''.join(track)

test = 'aabcccccaaa'

print(compress_string(test))