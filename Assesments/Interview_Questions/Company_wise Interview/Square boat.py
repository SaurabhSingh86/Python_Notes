"""
Square boat

1. Self Introduction
2. Why transformation from mechanical to computer science ?
3. Why you appllied to this job , do you know about this company ?
4. You have two rope with same size and same material and you can not  band and move . The property of the both
   rope is ,it is taking 1hr to burn complitly . But you are in room . so the condition is exactly at 46 mint
   the gate of the room will locked ,so you have to escape from the room at exact 45 min. so how can you
   calculate 45 minute by looking into burning rope , and remember you can not touch , move , bend the rope .
5. You have one cake , and in your bithday party only 8 peoples are there . You have only 3 chance to cut the
   cake with knife cutout with 8 pieces . there is no layer of cake , it means it is a sinle layer cake
6. Arr =[ 1,2,3,4,6,7,8 ]
   Write a function to find the index of 'n' number , if that is not present then on which place that suitable
   for ( index) , and after which number , and before which number that should be placed . n = 5
   n = 3
   And the output should be like this

   If n = 3 then  index will be 3
   If n = 7 then index will be 6
   If n = 5 then ,, it should shows output as ----  the number 5 is not present , so it is suitable for 5th
   position and it should place after 4 and before 6
7. Write a decorator function
8. What is Selenium web driver , why it is used ?
9. What is page object module ?
10.Wha is framework ?
11.How many types of frmaework is there ?
12.What is data driven framework ?
13.Have you ever worked on Framework designing ?
14.Tell me about framework designing ?
15.In selenium did you get any chance to use locators and selectors ?
16.what is locators ?
17.What is selectors ?
18.Can you write "product" in a google search text fieldby using selenium ?
19.Do you have any experience on CICD tool ?
20.Which tool you are using for automation ?


*Square-boat second-round questions*
1. Tell me about your project
2. Roles & responsibilities
3. What is the major difference between list & set
4. What is mutable & immutable data type
5. Merge two lists into a dictionary
6. what is zip?
7. How to handle multiple windows in selenium?
8. What's your project name is it a mobile application or web application?
9. What is Python procedure?
10. What is LEGB in Python?
11. What is the major drawback of a dictionary
12. What are 1 layer, 2 layer & 3 layers?
13. Difference between css & xpath
14. navigate web elements from a given website through a CSS selector
15. if the page is reloaded the value of the class is going to change how to handle this
16. What is API?
17. Codes stand for 401, 403, and 204?
18. What is get_window_handle?
19. What is the difference between get_window_handle & get_window_handles?
20. what type of library is used in Python?
21. Asked many real-based scenario questions (e.g in google pay if anyone gets 100 rs cashback then that cashback is automatically credited in the user's account, what is the procedure behind this?
22. what is a postman how does it works?
23. many more real-based questions related to API


1.Difference between selenium 3 and selenium4
2.about project explanation
3. Take Myntra website and Google website and ask what is the path and your mentioned in the website and why Myntra website is not secure and Google website is secure
4. What is desktop testing
5. What is mobile testing
6. What is a agile methodology
7. What you are going to automate in your project and how many scripts and test cases will you able to write  in one day
8.explain binary search and he gave a one list and asked to explain
9.scenario based questions all

1) severity vs priority with example
2) framework
3) json to python dictionary to fetch data
4) incase json file have duplicated keys without converting to dictionary find out duplicate keys
5) difference between selector and locator
6) which is faster
7) difference between keyword and data-driven framework
8)git commands
9) project management tool
10) how u raise bug in jira
11) open web page click operation on check box


1.what did you work on in your project?
2.what were the requirements from client in this duration?
3.where did you store the images of the application in your project?
4.How will you verify that image is correct or not?
5.what are the different functionalities on login page apart of username, password and login button?

6.how to declare the dictionary?
7.(a) programming question - create dictionary of item and occurance pair from list.
  (b) I did with one method, then he asked to do with another method, then asked to explain both the methods

8.Have you worked on database?
9.what is joins?
10.give any example of join?
11.on that example, he asked what if I give condition that salary is more than 10000?

12.what are the different git commands?

13.can we connect database through API?
14.How to connect database through API?
15.what are the rest API methods?
16.what are the different status codes in API?
17.what is the meaning of status code 404?
18.write api automation script?
19.what response is giving requests.get?
20.what json.loads is doing?
21.I have username and passowrd, after login button, if the username and password is correct, then I will get some ..... through API, if it is incorrect I will get error.
  (a) write the test cases for this scenario
  (b) he asked another qns on this, which I didnt understand

No questions asked from manual and selenium, he didnt even ask, tell me about yourself
"""

# l1 = [ 1, 2, 3]
# l2 = ["Shrihari", "saurabh", "Rama"]
#
# d = {key: value for key, value in zip(l1, l2)}
# print(d)


""" Write a program to get a list, sorted in increasing order by the last element in each tuple from a given list of
non-empty tuples. """

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# d = {i: j for i, j in l}
#
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res)


def sort_(item):
    item1, item2 = item
    return item2


res = sorted(l, key=sort_)
print(res)