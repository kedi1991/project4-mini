from taskmanager import db


class Category(db.Model):
    # schema for the category model
    id = db.column(db.Integer, primary_key=True)
    category_name = db.column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # to represent itself in form of a string.
        return self.category_name


class Task(db.Model):
    # schema for the task model
    id = db.column(db.Integer, primary_key=True)
    task_name = db.column(db.String(50), unique=True, nullable=False)
    task_description = db.column(db.Text, nullable=false)
    is_urgent = db.column(db.Boolean, default=False, nullable=False)
    due_date = db.column(db.Date, nullable=False)
    category_id = db.column(db.integer, db.ForeignKey(
        "category.id", ondelete="CASCADE", nullable=False))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, slef.is_urgent
        )