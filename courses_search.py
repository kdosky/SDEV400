# Name: Khoger Dosky
# File Name: courses_search.py
# Date: November 17, 2020
# Course: SDEV 400 7381 Secure Programming in the Cloud (2208)
# Dr. Matthew Taylor

# user input set to Y 
user_input = 'Y'

# code kept in while loop 
while user_input == 'Y':
    subject = input('Enter the Subject:\n')

    # if SDEV is selected 
    if subject == 'SDEV':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        # if catalog_nbr is not = to input 
        while catalog_nbr != '400':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            # if catalog_nbr is correct input 
            catalog_nbr = '400'
            print(f'The title of {subject} {catalog_nbr} is Secure Programming in the Cloud.')
        user_input = input('Would you like to search for another title? (Y or N)\n')
    
    # if ARTH is selected 
    elif subject == 'ARTH':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '334':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '334'
            print(f"The title of {subject} {catalog_nbr} is Understanding Movies.")
        user_input = input("Would you like to search for another title? (Y or N)\n")

    # if CCJS is selected 
    elif subject == 'CCJS':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '100':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '100'
            print(f"The title of {subject} {catalog_nbr} is Introduction to Criminal Justice.")
        user_input = input("Would you like to search for another title? (Y or N)\n")
    
    # if CMIS is selected 
    elif subject == 'CMIS':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '141':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '141'
            print(f"The title of {subject} {catalog_nbr} is Introductory Programming.")
        user_input = input("Would you like to search for another title? (Y or N)\n")
        
    # if CMST is selected 
    elif subject == 'CMST':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '290':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '290'
            print(f"The title of {subject} {catalog_nbr} is Introduction to Interactive Design.")
        user_input = input("Would you like to search for another title? (Y or N)\n")
    
    # if WRTG is selected 
    elif subject == 'WRTG':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '112':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '112'
            print(f"The title of {subject} {catalog_nbr} is Academic Writing II.")
        user_input = input("Would you like to search for another title? (Y or N)\n")        
    
    # if MATH is selected
    elif subject == 'MATH':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '105':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '105'
            print(f"The title of {subject} {catalog_nbr} is Topics for Mathematical Literacy.")
        user_input = input("Would you like to search for another title? (Y or N)\n")   
    
    # if STAT is selected
    elif subject == 'STAT':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '200':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '200'
            print(f"The title of {subject} {catalog_nbr} is Introduction to Statistics.")
        user_input = input("Would you like to search for another title? (Y or N)\n")  
    
    # if ACCT is selected
    elif subject == 'ACCT':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '326':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '326'
            print(f"The title of {subject} {catalog_nbr} is Accounting Information Systems.")
        user_input = input("Would you like to search for another title? (Y or N)\n") 
    
    # if ECON is selected
    elif subject == 'ECON':
        catalog_nbr = input('Enter the CatalogNbr:\n')
        while catalog_nbr != '201':
            catalog_nbr = input('A CatalogNbr is required. Enter the CatalogNbr:\n')
        else:
            catalog_nbr = '201'
            print(f"The title of {subject} {catalog_nbr} is Principles of Macroeconomics.")
        user_input = input("Would you like to search for another title? (Y or N)\n") 

    # if wrong subject is entered 
    else:
        subject != subject
        print("A Subject is required.")

# is N is selected as input 
if user_input == 'N':
    print("Thanks for using the Catalog Search program.")