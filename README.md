# Project Repository
https://github.com/Ali-M-Tabatabaei/online-car-store

![Local image](./images/main.png)


# Project Description
- an online car dealership website
- created using purely django
- no frontend framework used
- site functionality:
    - users can view each other's listed cars
    - users can put their own cars for sale

# Test Divisions
- signin/signup:Somayeh Ghorbani Moghaddam
- responsiveness:
- car search:
- dashboard:
- site navigation: علی وزیری نژاد (۹۹۱۲۷۶۲۴۹۴)


## signin/signup tests

## responsiveness tests

## car search tests
- test_search_car_asd:
    - Tests searching for a car with the keyword "asd". It verifies that one car is found.
- test_search_car_lamborgini:
    - Tests searching for a car with the keyword "lamborgini". It verifies that one car is found.
- test_search_car_by_model:
    - Tests searching for a car by selecting the model "r8" from a dropdown. It verifies that no cars are found.
- test_search_car_by_price: 
    - Tests searching for cars within a specified price range by adjusting price sliders. It verifies that no cars are found within the specified range.
- test_price_slider_lower_boundary: 
    - Tests the lower boundary of the price slider to ensure it increases when moved.
- test_price_slider_upper_boundary: 
    - Tests the upper boundary of the price slider to ensure it decreases when moved.
- test_search_car_by_city: 
    - Tests searching for cars in the city "Mashhad". It verifies that no cars are found.
- test_price_slider_lower_not_exceed_upper: 
    - Tests that the lower price boundary does not exceed the upper boundary.
- test_search_car_by_year: 
    - Tests searching for cars from the year "2020". It verifies that no cars are found.
- test_search_car_by_body_style: 
    - Tests searching for cars with the body style "racing". It verifies that no cars are found.
## dashboard tests

## site navigation tests (AliVazirinejad_9912762494)
- navbar_home_test:
    - tests whether the 'خانه' link in navbar redirects to the home page
- navbar_cars_test:
    - tests whether the 'ماشینها' link in the navbar redirects to the cars page
- navbar_services_test:
    - tests whether the 'سرویس ها' link in the navbar redirects to the services page
- navbar_about_test:
    - tests whehter the 'درباره' link in the navbar redirects to the about page
- navbar_contact_test:
    - tests whether the 'ارتباط با ما' link in the navbar redirects to the contact page
- car_test:
    - tests whether the sample car link in the car page, redirects to that very car's specifications page 
- car_send_message_test:
    - tests whether the 'ارسال پیام' modal in the car specification pop up when clicking on the 'ارسال پیام' button
- dashboard_not_logged_in_test:
    - tests whether clicking on the 'داشبورد' button on the navbar redirects to the login page when the user is not logged in
- demo:
    - a short video displaying the tests in execution
