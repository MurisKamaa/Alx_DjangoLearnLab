# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>


---

### **retrieve.md**
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)



---

### **update.md**
```markdown
# Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'



---

### **delete.md**
```markdown
# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
Book.objects.all()
# <QuerySet []>
