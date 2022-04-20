from db.models.post_content import Product
from schemas.post_contents import CreateProduct
from sqlalchemy.orm import Session

def create_new_post(post: CreateProduct, db: Session):
    post = Product(
        sku = post.sku,
        category_id = post.category_id,
        model = post.model,
        name = post.name,
        seo_title = post.seo_title,
        short_description = post.short_description,
        seo_description = post.seo_description,
        no_price_no_stock = post.no_price_no_stock,
        price = post.price,
        sort_priority = post.sort_priority,
        # image = post.image,
        content = post.content,
        disabled_by_vendoer = post.disabled_by_vendoer,
        disabled_by_admin = post.disabled_by_admin,
        require_user_login = post.require_user_login,
        # vendor_member_id = post.vendor_member_id,
        # vendor_company_id = post.vendor_company_id,
        created_at = post.created_at,
        content_updated_at = post.content_updated_at,
        popularity = post.popularity
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
