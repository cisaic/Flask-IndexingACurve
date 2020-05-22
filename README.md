# Flask-IndexingACurve

Project roadmap/history
-----------------------
1. Hackathon w ahmed
https://devpost.com/software/bounded-chaos

2. Continued to expand on GitHub
https://github.com/cisaic/Indexing-A-Space-Filling-Curve

3. Notice limitations in presentation 
- very difficult for others to understand
- code is difficult to just read like that when there's no dynamic element of /seeing what it does/

4. decide to create interactive user interface to demonstrate WHAT my code does and WHY it matters. Start researching Flask

5. Follow this tutorial to learn basic interaction of flask
https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=LLl5YN2s-K4GQu2MZ_2kKlCQ&index=2&t=0s 
> Enter virtual env (no long necessary with pycharm) 
$ source env/bin/activate 

6. Start reading documentation, figure out how to import functions from separate python script, for modularity
7. figure out pycharm
8. build a small form - display text you submit through form in html content
9. Spent a LOT off time trying to figure out how to import my own module into app.py
    * solution: mark flaskr directory as sources root, so import looks into this dir for python module
10. call curve_index function using user input as args
11. figure out how to explain what the project was and why it matters 
Why use hilbert curve? Why not generalize to any curve? 
Beauty is preservation of locality properties
Points lie close to each other - important for the applications of the hilbert curve
reach a limit as order increases - point at low resolution is very close to points at increasing depth
12. decide to only give user access to one alg

Why hilbert curve and not z curve or smth? Because hilbert has locality preservatino -> point reaches a limit

13. use ahmed's function to generate list of sequential sequences 
14. draw hilbert curve by converting sequences -> coordinates using my algo
15. plot a point on the curve!
16. generate slider so you can see how the point approximates a location as levels increase
- this also means I graph hilbert curve at each level up to length of sequence input
17. plot 3d hilbert curve!!
18. plot 3d hilbert curve with step that moves dot through sequential points
-> using index_curve2 instead of hardcoded function
19. try to figure out how to make color gradient follow sequential order instead of linear scale along one axis
    - couldn't figure it out
21. save 3d hilbert coordinates as json/csv file for easier access
    - couldn't figure out how to save plotly JSONEncoder to json file and just read from there
22. load plotly files directly on index page (instead of opening in new tab)
23. start with sample 2d slider


# TODO
- Limit input length! 
- search animations
- point on nxm graph with z-curve (or some other orthant-order-sequence) (?)
- line color gradient that is sequential not along one axis
- describe what's going on
- generate necessary csv/json for sample graphs
- comment code! clean up! standardize naming!!!
- styling 
- add 3d hilbert at order 1
- make 2d hilbert with multiple levels on same graph
- disable zoom on graphs so scrolling doesnt get affected
