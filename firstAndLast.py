# given a list of people this will print there title and last name 

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return (person.split(' '))[0], (person.split(' '))[-1]

list(map(split_title_and_name, people))
