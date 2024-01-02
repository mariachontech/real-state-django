# Generated by Django 5.0.1 on 2024-01-02 21:51

import django_countries.fields
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+529867236644",
                        max_length=30,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "about_me",
                    models.TextField(
                        default="Say something about you", verbose_name="About Me"
                    ),
                ),
                (
                    "license",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Real State License",
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        default="/profile_default.png",
                        upload_to="",
                        verbose_name="Profile Photo",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=20,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="KE", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Nairobi", max_length=180, verbose_name="City"
                    ),
                ),
                (
                    "is_buyer",
                    models.BooleanField(
                        default=False,
                        help_text="Are you looking to buy a propery",
                        verbose_name="Buyer",
                    ),
                ),
                (
                    "is_seller",
                    models.BooleanField(
                        default=False,
                        help_text="Are you looking to sell a propery",
                        verbose_name="Seller",
                    ),
                ),
                (
                    "is_agent",
                    models.BooleanField(
                        default=False,
                        help_text="Are you an agent",
                        verbose_name="Agent",
                    ),
                ),
                (
                    "top_agent",
                    models.BooleanField(
                        default=False,
                        help_text="Are you a top agent",
                        verbose_name="Top Agent",
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, max_digits=4, null=True),
                ),
                (
                    "num_reviews",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="Number of Reviews",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
