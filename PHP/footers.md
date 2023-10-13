https://medium.com/@dtkahn/sharing-headers-and-footers-across-multi-page-websites-4396f9034669

Certainly! To reuse a header and footer in PHP, you can create separate files for the header and footer and then include them in your main PHP files where needed. Here's a basic example:

1. **header.php**
   ```php
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Your Website</title>
       <!-- Include your CSS files or other head elements here -->
   </head>
   <body>
       <!-- Your header content goes here -->
       <header>
           <h1>Welcome to Your Website</h1>
           <!-- Other header content -->
       </header>
   ```

2. **footer.php**
   ```php
       <!-- Your footer content goes here -->
       <footer>
           <p>&copy; <?php echo date("Y"); ?> Your Website. All rights reserved.</p>
           <!-- Other footer content -->
       </footer>
   </body>
   </html>
   ```

3. **index.php (or any other main file)**
   ```php
   <?php include 'header.php'; ?>

   <!-- Your main content goes here -->
   <div>
       <p>This is the main content of your page.</p>
   </div>

   <?php include 'footer.php'; ?>
   ```

In this example, the `include` statement is used to include the content of `header.php` and `footer.php` in the `index.php` file. This way, you can reuse the header and footer across multiple pages by including them where needed.

Make sure that the paths in the `include` statements are correct based on your file structure. This is a simple example, and in a real-world scenario, you might want to consider using functions, classes, or more sophisticated templating engines based on the complexity of your application.
