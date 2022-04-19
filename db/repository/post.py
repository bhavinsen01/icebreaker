from db.models.post_content import PostContents, SubCategory
from schemas.post_contents import PostCreate, SubCategories
from sqlalchemy.orm import Session

def create_new_post(post: PostCreate, db: Session):
    post = PostContents(
        sku = post.sku,
        url = post.url,
        service_name = post.service_name,
        service_short_description = post.service_short_description,
        price = post.price,
        availibility = post.availibility,
        post_category = post.post_category
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def create_sub_category(sub_category_types: SubCategories, db: Session):
    print("======", sub_category_types.sub_category_title)
    sub_category = SubCategory(
        sub_category_name = sub_category_types.sub_category_title
    )
    db.add(sub_category)
    db.commit()
    db.refresh(sub_category)
    return sub_category