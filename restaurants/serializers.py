from datetime import date

from rest_framework import serializers

from restaurants.models import Restaurant, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(
        source="restaurant.name", read_only=True
    )
    vote_count = serializers.ReadOnlyField()

    class Meta:
        model = Menu
        fields = [
            "id",
            "date",
            "menu_detail",
            "restaurant",
            "restaurant_name",
            "vote_count",
        ]


class VoteSerializerV1(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.filter(date=date.today())
    )

    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ["employee"]

    def create(self, validated_data):
        menu = validated_data.get("menu")

        user = self.context["request"].user

        menu.vote_count += 1
        menu.save()

        validated_data["employee"] = user
        return super().create(validated_data)


class VoteSerializerV2(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.filter(date=date.today())
    )

    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ["employee"]

    def create(self, validated_data):
        menu = validated_data.get("menu")

        # Checking whether user has already voted for the menu
        user = self.context["request"].user
        if Vote.objects.filter(employee=user, menu=menu).exists():
            raise serializers.ValidationError(
                "You have already voted for this menu."
            )

        menu.vote_count += 1
        menu.save()

        validated_data["employee"] = user
        return super().create(validated_data)


class MostChosenMenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source="restaurant.name")
    vote_count = serializers.SerializerMethodField()

    def get_vote_count(self, obj):
        return obj.vote_count

    class Meta:
        model = Menu
        fields = [
            "id",
            "restaurant",
            "restaurant_name",
            "date",
            "menu_detail",
            "vote_count",
        ]
