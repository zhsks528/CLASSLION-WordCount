from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}
    word_dict_duplicate = {}
    word_dict_no = {}

    for word in words:
        if (word in word_dict):
            #increase
            word_dict[word] += 1

        else:
            # add to dictionary
            word_dict[word] = 1

    # 중복여부
    for value in word_dict:
        if (word_dict[value] >= 2):
            # 중복 O
            word_dict_duplicate[value] = word_dict[value]
        else:
            # 중복 X
            word_dict_no[value] = word_dict[value]

    return render(
        request, 'result.html', {
            'full': text,
            'total': len(words),
            'dict': word_dict.items(),
            'dict_duplicate': word_dict_duplicate.items(),
            'dict_no': word_dict_no.items()
        })
