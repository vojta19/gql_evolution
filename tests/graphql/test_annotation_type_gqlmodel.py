from src.GraphTypeDefinitions.schema_factory import create_schema


def test_annotation_type_is_reachable_through_graphql_schema():
    schema = create_schema()
    schema_sdl = schema.as_str()

    assert "annotationTypeById" in schema_sdl
    assert "annotationTypePage" in schema_sdl
    assert "annotationTypeInsert" in schema_sdl
    assert "annotationTypeUpdate" in schema_sdl
    assert "annotationTypeDelete" in schema_sdl
    assert "annotation_type_id" in schema_sdl
    annotation_type = schema._schema.type_map["AnnotationTypeGQLModel"]
    assert "annotations" in annotation_type.fields
