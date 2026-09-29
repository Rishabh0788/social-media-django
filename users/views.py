from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Profile

from .forms import (
    RegisterForm,
    ProfileForm
)


def register_view(request):

    if request.user.is_authenticated:

        return redirect("home")


    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            Profile.objects.create(
                user=user
            )

            login(
                request,
                user
            )

            return redirect("home")

    else:

        form = RegisterForm()


    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.user.is_authenticated:

        return redirect("home")


    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect("home")


        return render(
            request,
            "login.html",
            {
                "error":
                "Invalid username or password."
            }
        )


    return render(
        request,
        "login.html"
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def profile_view(
    request,
    username
):

    profile_user = get_object_or_404(
        User,
        username=username
    )


    profile, created = Profile.objects.get_or_create(
        user=profile_user
    )


    if (
        request.method == "POST"
        and request.user == profile_user
    ):

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )


        if form.is_valid():

            form.save()

            return redirect(
                "profile",
                username=username
            )

    else:

        form = ProfileForm(
            instance=profile
        )


    posts = profile_user.posts.all()


    is_following = False


    if request.user != profile_user:

        is_following = profile.followers.filter(
            id=request.user.id
        ).exists()


    return render(
        request,
        "profile.html",
        {
            "profile_user":
                profile_user,

            "profile":
                profile,

            "posts":
                posts,

            "form":
                form,

            "is_following":
                is_following
        }
    )


@login_required
def follow_user(
    request,
    username
):

    target_user = get_object_or_404(
        User,
        username=username
    )


    if request.user == target_user:

        return redirect(
            "profile",
            username=username
        )


    profile = target_user.profile


    if profile.followers.filter(
        id=request.user.id
    ).exists():

        profile.followers.remove(
            request.user
        )

    else:

        profile.followers.add(
            request.user
        )


    return redirect(
        "profile",
        username=username
    )