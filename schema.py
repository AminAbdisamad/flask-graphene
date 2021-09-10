import graphene
from graphene.types.schema import Schema


class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.Argument(graphene.String, default_value="World")
    )

    def resolve_hello(self, info, name):
        return "Hello " + name


hello_schema = graphene.Schema(query=Query)


my_query = """
    {
        hello ( name : "Ali")
    }
"""

query_result = hello_schema.execute(my_query)


class Book(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int)
    title = graphene.String
    author = graphene.String


class BookQuery(graphene.ObjectType):
    book = graphene.Field(Book)

    def resolve_book(self, info):
        print(info)
        return Book(id=1, title="My book", author="Ali Jama")


book_query = """
{
    book {
        id, title
    }
}
"""
book_schema = graphene.Schema(query=Book)
book_result = book_schema.execute(query=book_query)
