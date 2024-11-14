import random


when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'In my childhood', 'During the summer vacation', 'In the distant future', 'Once upon a time']
who = ['a clever rabbit', 'a wise elephant', 'a curious mouse', 'a slow turtle', 'a mischievous cat', 'a majestic lion', 'a loyal dog', 'a playful monkey', 'a cuddly bear', 'a colorful bird', 'a graceful giraffe', 'a hopping kangaroo', 'a peaceful panda']
residence = ['India', 'Barcelona', 'Germany', 'Venice', 'England', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Rio de Janeiro', 'Moscow', 'Cairo']
went = ['cinema', 'university', 'seminar', 'school', 'laundry', 'zoo', 'park', 'beach', 'restaurant', 'hospital', 'library', 'gym', 'market', 'concert']
happened = ['made a lot of friends', 'ate a delicious burger', 'found a mysterious key', 'solved a challenging mystery', 'wrote an inspiring book', 'learned a new language', 'built a cozy house', 'won a prestigious competition', 'started a successful business', 'adopted a cute pet']

    
print(random.choice(when) + ' , ' + random.choice(who) + ' lived in ' +
random.choice(residence) + ' One ' + random.choice(when) + ', they decided to visit the ' + random.choice(went) +
'. While walking to the ' + random.choice(went) + ', they encountered ' + random.choice(who) + '. hey decided to team up and continued their journey...')
    

    

