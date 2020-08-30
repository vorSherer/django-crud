# Lab 28 - Django CRUD

### *Author: Thomas Sherer*, 2020-08-29

---

## Description
### Feature Tasks and Requirements
*NOTE: replace __`blog`__ and __`Post`__ with your own names.*

- [X] Create __`blog_project`__ Django project <br>
- [X] Create __`blog`__ app <br>
- [X] Create __`Post`__ model <br>
	- [X] title field <br>
	- [X] author field <br>
	- [X] body field <br>
	- [X] Register model with admin <br>

- [X] Create __`BlogListView`__ that extends appropriate generic view <br>
	- [X] associated url path is an empty string <br>

- [X] Create __`BlogDetailView`__ that extends appropriate generic view <br>
	- [X] associated url path is __`post/<int:pk>/`__ <br>

- [ ] Create __`BlogCreateView`__ that extends appropriate generic view <br>
	- [X] associated url path is __`post/new/`__ <br>

- [ ] Create __`BlogUpdateView`__ that extends appropriate generic view <br>
	- [ ] associated url path is __`post/<int:pk>/edit/`__ <br>

- [ ] Create __`BlogDeleteView`__ that extends appropriate generic view <br>
	- [ ] associated url path is __`post/<int:pk>/delete/`__ <br>

- [ ] Add urls to support all views, with appropriate names <br>
- [ ] Add templates to support all views <br>
- [ ] Add navigation links in appropriate locations to access all pages <br>
- [ ] Make all necessary changes to project level files for project to run <br>
	- In other words, make it work <br>

## Implementation Notes
- A lot of functionality is being added here. But it should still follow the “Django way.” So when in doubt refer back to demo. <br>

---

### Collaborations and Attributions
<!-- __Skyler Burger__ helped immensely with NN. -->

__Merry Cimakasky__ helped with Django Form implementation.

<!-- __Lee-Roy King__ helped with NN. -->

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/django

---
