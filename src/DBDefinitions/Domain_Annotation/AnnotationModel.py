import typing
import datetime
import dataclasses
import sqlalchemy

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, synonym
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, column_property

from src.DBDefinitions.BaseModel import BaseDBModel, UUIDColumn, UUIDFKey, IDType


class AnnotationModel(BaseDBModel):
    __tablename__ = "annotations"

    # Identifikátor anotované entity
    entity_id: Mapped[IDType] = mapped_column(
        nullable=False,
        index=True,
    )

    # Typ anotované entity
    entity_type_id: Mapped[IDType] = mapped_column(
        nullable=False,
        index=True,
    )

    # Název anotace
    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    # Vlastník anotace
    owner_id: Mapped[IDType] = mapped_column(
        nullable=False,
        index=True,
    )

    # Text anotace
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )