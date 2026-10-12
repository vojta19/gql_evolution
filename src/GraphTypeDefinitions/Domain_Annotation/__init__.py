import strawberry

from .AnnotationGQLModel import (
    AnnotationGQLModel,
    AnnotationInputFilter,
    AnnotationMutation,
    AnnotationQuery,
)


@strawberry.interface(description='Annotation domain queries')
class Query_Annotation(AnnotationQuery):
    pass


@strawberry.interface(description='Annotation domain mutations')
class Mutation_Annotation(AnnotationMutation):
    pass


__all__ = [
    'AnnotationGQLModel',
    'AnnotationInputFilter',
    'Query_Annotation',
    'Mutation_Annotation',
]