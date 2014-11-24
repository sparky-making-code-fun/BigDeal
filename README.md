BigDeal
=======

Project BigDeal Repo


Set Up Virtualenv
=================


From the command line run mkvirtualenv bigdeal

GitFlow
=======

This project uses a slightly modified git flow type workflow. 

1) Each feature or fix should be created in it's own branch branching from master. 
2) Upon completing the code for a feature or fix you should merge master INTO your feature/fix branch
e.g. 
git checkout <my branch>
git merge master
#This merges any changes that were pushed to the master branch into your feature/fix branch
#Now you need to resolve any merge issues. 
#Then run the unittests and make sure every thing still passes

3) When any merge issues are resolved and the unittests all pass go to github and create a merge request for
your branch. 



Commit Comments
===============

Commit comments are integrated between Github and Yodiz. 

Please read here and follow the guidelines

http://app.yodiz.com/thirdparty/pages/git.vz

