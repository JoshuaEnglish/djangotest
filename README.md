# djangotest
Troubleshooting Django issues


## limit

In my propriety app that I'm building for my employer, I ran into
a problem where the admin screen is not limiting my choice in creating
a sales team.

This app builds up the basic model and does work in the basic app.


## import_text_choices

This was a failed attempt to get use a TextChoice object for a "status" field
and also get the thing to work with ``django-filters``. I gave up getting this
to work and decided to change the TextChoice to its own Model

## migration_with_data_swap

Having decided to change things at the field level but not wanting to delete
the database and start over, I created a custom migration step with the 
encouragement of Redditors.
