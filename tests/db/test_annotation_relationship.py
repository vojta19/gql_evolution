from sqlalchemy import inspect

from src.DBDefinitions import AnnotationModel, AnnotationTypeModel


def test_annotation_type_is_linked_by_foreign_key():
    annotation_type_id = AnnotationModel.__table__.c.annotation_type_id

    assert {foreign_key.target_fullname for foreign_key in annotation_type_id.foreign_keys} == {
        "annotationtypes.id"
    }


def test_annotation_type_relationship_is_bidirectional():
    annotation_relationship = inspect(AnnotationModel).relationships["annotation_type"]
    type_relationship = inspect(AnnotationTypeModel).relationships["annotations"]

    assert annotation_relationship.uselist is False
    assert annotation_relationship.back_populates == "annotations"
    assert type_relationship.uselist is True
    assert type_relationship.back_populates == "annotation_type"
