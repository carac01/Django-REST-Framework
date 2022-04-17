### Flow

You remember and automate a lot of testing mechanisms with practice.
I suggest the route - probably it could be valuable for you also:

1. Document the Endpoints
2. Create Tests.
3. Define the model.
4. Define the views.
5. Define the serializers.   
6. Register the route.
7. Execute the tests.

If you work in a team - everything is changed, because you should support the flow, 
creating readable CI/CD pipeline.

1. Create the branch.
2. Document the Endpoints (Andros likes Notion).
3. Create the test (Andros works with Pytest).
4. Define the model.
5. Define the views.
6. Define the serializers.   
7. Register the route.   
8. Use linter (Andros adores Black).
9. Execute the test.
10. Configure the Admin.
11. Merge Request: add the changes to repository and ask the colleague from your team to review it.
12. CI/CD: the conflicts will be checked automatically. 
    If everything works as expected and there are no conflicts - the changes will be added to master branch.
    
I hope you will find the information valuable.
