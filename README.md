# Lab 28 - Django CRUD

### *Author: Thomas Sherer*, 2020-08-29

---

## Description
### Feature Tasks and Requirements
NOTE: replace __`blog`__ and __`Post`__ with your own names.

# Lab 28 - Django CRUD

### *Author: Thomas Sherer*, 2020-08-29

---

## Description
### Feature Tasks and Requirements
*NOTE: replace __`blog`__ and __`Post`__ with your own names.*

-[X] Create __`blog_project`__ Django project
-[X] Create __`blog`__ app
-[ ] Create __`Post`__ model
	-[ ] title field
	-[ ] author field
	-[ ] body field
	-[ ] Register model with admin <br>

-[ ] Create __`BlogListView`__ that extends appropriate generic view
	-[ ] associated url path is an empty string <br>

-[ ] Create __`BlogDetailView`__ that extends appropriate generic view
	-[ ] associated url path is __`post/<int:pk>/`__ <br>

-[ ] Create __`BlogCreateView`__ that extends appropriate generic view
	-[ ] associated url path is __`post/new/`__ <br>

-[ ] Create __`BlogUpdateView`__ that extends appropriate generic view
	-[ ] associated url path is __`post/<int:pk>/edit/`__ <br>

-[ ] Create __`BlogDeleteView`__ that extends appropriate generic view
	-[ ] associated url path is __`post/<int:pk>/delete/`__

-[ ] Add urls to support all views, with appropriate names
-[ ] Add templates to support all views
-[ ] Add navigation links in appropriate locations to access all pages
-[ ] Make all necessary changes to project level files for project to run
	- In other words, make it work <br>

## Implementation Notes
- A lot of functionality is being added here. But it should still follow the “Django way.” So when in doubt refer back to demo. <br>

---

### Collaborations and Attributions
<!-- __Skyler Burger__ helped immensely with NN. -->

<!-- __Merry Cimakasky__ helped with NN. -->

<!-- __Lee-Roy King__ helped with NN. -->

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/django

<!-- __likegeeks.com__ helped with [understanding chr() and ord()](https://likegeeks.com/python-caesar-cipher/) -->

---
