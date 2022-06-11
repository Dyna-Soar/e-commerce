# E-Commerce

### This is the business logic of an ecommerce django application. Using modular architecture and domain driven design.
### Full stack developers can integrate their templates into the already written backend application.

### Domains
- Clients
- Products
- Orders

### Features:
- Client operations
- Product operations
- Newsletter operations
- Admin/staff panel
- TODO cart stored in session
- TODO stripe's payment api
- MAYBE data analytics

### Testing
Every domain/app comes with a set of unit and functional tests, using built-in django TestCase instances.

To run tests enter `python manage.py test` or `python manage.py tests appname`