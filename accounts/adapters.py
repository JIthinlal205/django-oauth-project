# accounts/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        # Extract extra payload data returned by the provider
        extra_data = sociallogin.account.extra_data
        
        if sociallogin.account.provider == 'google':
            user.first_name = extra_data.get('given_name', '')
            user.last_name = extra_data.get('family_name', '')
        elif sociallogin.account.provider == 'github':
            full_name = extra_data.get('name', '')
            if full_name:
                parts = full_name.split(' ', 1)
                user.first_name = parts[0]
                user.last_name = parts[1] if len(parts) > 1 else ''
        elif sociallogin.account.provider == 'facebook':
            user.first_name = extra_data.get('first_name', '')
            user.last_name = extra_data.get('last_name', '')
            
        return user