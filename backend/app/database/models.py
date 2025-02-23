from datetime import datetime, UTC
from typing import List
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    mapped_column,
    relationship,
)

Base = declarative_base()


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(5), unique=True)  # e.g., 'en', 'pt-BR'
    name: Mapped[str] = mapped_column(String)  # e.g., 'English', 'Portuguese (Brazil)'
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    avatar_id: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    translations: Mapped[List["CardTranslation"]] = relationship(
        back_populates="card", cascade="all, delete-orphan"
    )
    spoilers: Mapped[List["Spoiler"]] = relationship(
        back_populates="card", cascade="all, delete-orphan"
    )


class CardTranslation(Base):
    __tablename__ = "card_translations"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=False)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"), nullable=False)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    card: Mapped["Card"] = relationship("Card", back_populates="translations")
    language: Mapped["Language"] = relationship("Language")


class Spoiler(Base):
    __tablename__ = "spoilers"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    card: Mapped["Card"] = relationship("Card", back_populates="spoilers")
    translations: Mapped[List["SpoilerTranslation"]] = relationship(
        back_populates="spoiler", cascade="all, delete-orphan"
    )


class SpoilerTranslation(Base):
    __tablename__ = "spoiler_translations"

    id: Mapped[int] = mapped_column(primary_key=True)
    spoiler_id: Mapped[int] = mapped_column(ForeignKey("spoilers.id"), nullable=False)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    spoiler: Mapped["Spoiler"] = relationship("Spoiler", back_populates="translations")
    language: Mapped["Language"] = relationship("Language")


class SpoilerSeen(Base):
    __tablename__ = "spoilers_seen"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    spoiler_id: Mapped[int] = mapped_column(ForeignKey("spoilers.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )


class CardAnswered(Base):
    __tablename__ = "cards_answered"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    card_id: Mapped[int] = mapped_column(ForeignKey("cards.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )
