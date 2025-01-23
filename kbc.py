print('Hello today we are going to play KBC \n What\'s your name?')
q=['Q1. Which of the following countries is the world\'s largest producer of saffaron?','Q2. Which god is also known as ‘Gauri Nandan’?','Q3. What does not grow on tree according to a popular Hindi saying?','Q4. Which city is known as the Pink City of India?']
a=['b','d','a','c']
op = [['Spain','Iran','India','Greece'],['Agni','Indra','Hanuman','Ganesha'],['Money','Flowers','Leaves','Fruits'],['Banglore','Mysore','Jaipur','Kochi']]
name = input()
print('Welcome to KBC mini', name)
p = ['10 Lakh','50 Lakh','1 Crore','5 Crore']
for i in range(len(q)):
    
     print('Here is your question for', p[i],'rupees')
     print(q[i])
     print('a)',op[i][0],'            ','b)',op[i][1],'\nc)',op[i][2],'            ','d)',op[i][3])
     print('Choose the correct option a b c d')
     ans = input('Enter your answer : ')
     if(ans == a[i]):
         print('Congratulations! You have won', p[i],'rupees')
         if(i==3):
             print('You have become a Crorepati')
             break
     else:
         print('Sorry! You have given wrong answer')
         break
print('It was nice playing with you', name)
