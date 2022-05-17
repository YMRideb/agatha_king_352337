Checklist for final project presentations and job stuff later
    1) Create a wireframe
    2) Create clickable prototype using HTML, CSS front end
    3) Create ERD
    4) Always a good idea to show these before demo-ing functionality
*******************************************************************************
"Intro to ERD"
 - 9:00 in is when the ERD diagram is looking good and gets better
*******************************************************************************
```js
// If you were working for a major grocery store, where might you see a one-to-one relationship in their database?
//One to many?
//Many to many?
1) Any given customer_id is tied to their membership_id, typically with a phone number
2) Any specific candy_item can be located at many different locations, but any location only holds one candy_item
3) Any given brand_name can have different sale_items, and any given sale_items can belong to any given brand_names
```
*******************************************************************************
```py
**mySQL > Conventions ==
Guidelines

Down the line, you may find yourself working with a company that has set up their database conventions a little bit differently, but these are the guidelines that we feel are best for this course:

    1)make the table name plural and ALL lowercase - make it plural (ex. users, leads, sites, clients, chapters, courses, modules)
    2)use "id" as the primary key - name it id (also make it auto-incremented).
    3)name foreign keys with singular_table_name_id when referencing to a primary key in another table name it [singular name of the table youre referring to]_id (ex. user_id, lead_id, site_id, client_id, chapter_id, course_id, module_id).
    4)use created_at and updated_at as columns for the timestamp in EVERY table you create.

When we do things in ORM or in Ruby on Rails, it becomes extremely important that we follow these naming conventions
```