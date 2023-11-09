from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(2, "Name must be at least 2 characters long."),
            validators.MaxLengthValidator(100, "Name cannot exceed 100 characters.")]
    )

    location = models.CharField(
        max_length=200,
        validators=[
            validators.MinLengthValidator(2, "Location must be at least 2 characters long."),
            validators.MaxLengthValidator(200, "Location cannot exceed 200 characters.")]
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0, "Rating must be at least 0."),
            validators.MaxValueValidator(5, "Rating cannot exceed 5.")]
    )


def validate_menu_categories(value):
    required_categories = ["Appetizers", "Main Course", "Desserts"]

    for category in required_categories:
        if category.lower() not in value.lower():
            raise ValidationError(f'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        validators=[validate_menu_categories]
    )

    restaurant = models.ForeignKey(to='Restaurant',
                                   on_delete=models.CASCADE)


class ReviewMixin(models.Model):
    rating = ...
    review_content = ...

    class Meta:
        abstract = True
        ordering = ['-rating']


class RestaurantReview(models.Model):
    reviewer_name = models.CharField(
        max_length=100,
    )

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )

    review_content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ["reviewer_name", "restaurant"]

        abstract = True


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"
        unique_together = ["reviewer_name", "restaurant"]


class MenuReview(models.Model):
    reviewer_name = models.CharField(
        max_length=100,
    )

    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE,
    )

    review_content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ['reviewer_name', 'menu']
        indexes = [models.Index(
            fields=['menu'],
            name='main_app_menu_review_menu_id'
        )]







