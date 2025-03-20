# student={"name":"Alice","age":25,"grade":"A"}
# for key,value in student.items():
#     print(key,":",value)


# student={"name":"Alice","age":25,"grade":"A"}
# items=list(student.items())
# print(items)


# scores={"Alice":85,"Bob":90,"Charlie":80}
# sorted_score=sorted(scores.items(),key=lambda x:x[1])
# print(sorted_score)


# scores={"Alice":85,"Bob":90,"Charlie":80}
# high_scores={k:v for k,v in scores.items() if v > 85}
# print(high_scores)


# scores={"Alice":85,"Bob":90,"Charlie":80}
# highest=max(scores.items(), key=lambda x:x[1])
# lowest=min(scores.items(), key=lambda x:x[1])
# print(highest)
# print(lowest)


# scores={"Alice":85,"Bob":90,"Charlie":80}
# new_value={k:v+5 for k, v in scores.items()}
# new_key=scores.keys()
# new_val=scores.values()
# print(new_key)
# print(new_val)
# print(new_value)


# sentence="apple banana apple orange banana apple"
# words=sentence.split()
# print(words)
# word_count={}
# for word in words:
#     word_count[word]=word_count.get(word,0)+1
# for word, count in word_count.items():
#     print(f"{word}:{count}")


# sentence="this is a sample sentence and this sentence is just a sample"
# word_count={}
# for word in sentence.split():
#     word_count[word]=word_count.get(word,0)+1
# print(word_count)    
# for word,count in word_count.items():
#     print(f"{word}:{count}")    


# students={
#     "Alice":{"Math":85,"Science":92,"English":88},
#     "Bob":{"Math":78,"Science":80,"English":75},
#     "Charlie":{"Math":90,"Science":85,"English":95}
# }

# for student,subjects in students.items():
#     print(f"{student}:{subjects}")


# phonebook={
#     "John":"111-111-1111",
#     "Alice":"222-222-2222",
#     "Bob":"333-333-3333"
# }
# phonebook["Charlie"]="444-444-4444"

# name=input("Enter the name: ").title()
# print(f"Phone number:{phonebook.get(name,'not found')}")



# orginal_dict={"a":1,"b":2,"c":3}
# reversed_dict={v:k for k,v in orginal_dict.items()}
# print(reversed_dict)


# dict1={"a":1,"b":2}
# dict2={"c":3,"d":4}
# marged_dict={**dict1,**dict2}
# print(marged_dict)


# numbers=[1,3,2,3,4,2,3,5,2,2]
# frequency={}

# for num in numbers:
#     frequency[num]=frequency.get(num,0)+1
# most_frequent=max(frequency,key=frequency.get)
# print(frequency)
# print(f"Most frequent number:{most_frequent} (appears {frequency[most_frequent]} times)")


# documents={
#     "doc1":"Python is great",
#     "doc2":"Python and Java are popular",
#     "doc3":"I love coding in python"
# }
# inverted_index={}
# for doc, text in documents.items():
#     for word in text.split():
#         word=word.lower()
#         # print(inverted_index)        
#         if word not in inverted_index:
#             inverted_index[word]=[]
#         inverted_index[word].append(doc)
# print(inverted_index)   



# data={"apple":3,"banana":1,"cherry":2}
# sorted_data=dict(sorted(data.items(),key=lambda item:item[1]))
# print(sorted_data)


# keys=["name","age","city"]
# values=["Alice",25,"New York"]
# person=dict(zip(keys,values))
# print(person)


# scores={"Alice":89,"Bob":92,"Charlie":85}
# top_scorer=max(scores,key=scores.get)
# print(f"Top scorer:{top_scorer} with {scores[top_scorer]} points")


#last line