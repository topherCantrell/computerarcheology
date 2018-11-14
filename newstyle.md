The "new style" (won't be new for long) is to keep as closely to pure markdown as possible.

Here are the details as I flesh them out.

# General Structure

The landing page of a directory is `README.md`. On the web site, every page has a title and image at the top. Every page has a navigation
title that might be different (shorter) than the page's title.

```
![](Madness.jpg)
<!-- navTitle Madness & Minotaur -->
# Madness and the Minotaur
```
The page must start with an image link. This becomes the page's title image. The page's title is the first single-hash
tag. The `navTitle` comment specifies the navigation title. If not given, the page title is used for navigation.

# Special Areas

The web page allows for special areas like "Play Me" and "Tour Guide". These areas are wrapped in comment blocks like this:

```
<!-- playMe { -->
<!-- } -->

<!-- tourGuide { -->
<!-- } -->
```

Sections of HTML can be inserted in the markdown like this:

```
    ```html
    <hr>    
    ```
```

Sections of code are placed in code blocks:
```
    ```code
    This is some code
    ````
```

# Address Maps

