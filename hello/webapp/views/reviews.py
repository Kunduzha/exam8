from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Review, Goods
from webapp.forms import ReviewForms

class AllReviews(ListView):
    template_name = 'Review/index.html'
    model = Review
    context_object_name = 'reviews'



class AddReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'Review/add_review.html'
    form_class = ReviewForms



    def get_success_url(self):
        return reverse('see_good', kwargs={'good_pk':self.object.pk})



class ReviewUpdate(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'Review/update_review.html'
    form_class= ReviewForms
    context_object_name = 'review'
    permission_required = 'webapp.change_review'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().good.reviews.user.all()

    def get_success_url(self):
        return reverse('see_good', kwargs={'pk': self.object.good.pk})


class DeleteReview(PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().good.review.user.all()
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('see_good', kwargs={'pk': self.object.good.pk})
