def convert_to_digit(n,suffix): #Function to get the integer values from list and add it to the final string
    if n == 0: return ''  #returning empty string if there are no digits after floor division by the respective crore
    if n > 19: return Y[n // 10] + X[n%10] + suffix 
    else: return X[n] + suffix
def convert(n): #Function to make a string value of the integer number to word form
    final_word = convert_to_digit((n // 10000000) % 100, 'Crore ') #Floor division by 1 crore to get the indexes and index into the lists and add it to the final string
    final_word += convert_to_digit((n // 100000) % 100, 'Lakh ') #Floor division by 1 lakh to get the indexes and index into the lists and add it to the final string
    final_word += convert_to_digit((n // 1000) % 100, 'Thousand ') #Floor division by 1 thousand to get indexers and index into the lists and add it to the final string
    final_word += convert_to_digit((n // 100) % 10, 'Hundred ') #Floor division by 100 to get indexes and index into the lists and add it to the final string
    final_word += convert_to_digit((n % 100), '') #Modula by 100 to get indexes for indexing into the lists and add it to the final string
    return final_word

#Drivers Code
if __name__=='__main__':
    X = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ',  'Six ', 'Seven ','Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ','Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
    Y = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ','Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
    n = int(input("Enter any number between 0 and 99 crore : "))
    print(convert(n))